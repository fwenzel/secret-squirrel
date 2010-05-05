from urlparse import urlparse

from django.http import HttpResponseForbidden

import cas_provider.views

from .models import ClientSite


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
        return HttpResponseForbidden('Invalid service URL.')
    else:
        return cas_provider.views.login(request, *args, **kwargs)
