import logging
from urlparse import urlparse

from django.http import HttpResponseForbidden, HttpResponseRedirect

import cas_provider.views

from .models import ClientSite


log = logging.getLogger('sso.login')


def whitelist_login(request, *args, **kwargs):
    """
    Run service requests against whitelist before serving them through the
    CAS provider.
    """
    service = request.GET.get('service', '')
    parsed = urlparse(service)
    if not service or not parsed.netloc:
        return cas_provider.views.login(request, *args, **kwargs)

    try:
        site = ClientSite.objects.get(domain=parsed.netloc)
    except ClientSite.DoesNotExist:
        log.warning('Login request for invalid service URL %s' % service)
        return HttpResponseForbidden('Invalid service URL.')

    response = cas_provider.views.login(request, *args, **kwargs)

    # Associate user with this service
    if (request.user.is_authenticated() and
        isinstance(response, HttpResponseRedirect)):
            try:
                usersite = request.user.sites.get(pk=site.pk)
            except ClientSite.DoesNotExist:
                site.users.add(request.user)
                log.debug(
                    'First-time association of user %s with service %s' % (
                        request.user.username, site.domain))
    return response
