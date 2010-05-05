from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    ('', include('sso.urls')),

    # Hook up login/logout separately from the following apps

    # Login through service whitelist
    url(r'^users/login/?$', 'sso.views.whitelist_login'),
    url(r'^users/logout/?$', 'cas_provider.views.logout', {
        'template_name': 'users/logout.html'}),

    # order is important here: If both apps provide a URL, only the first one
    # will match.
    (r'^users/', include('cas_provider.urls')),
    (r'^users/', include('registration.urls')),

    (r'^profile/', include('users.urls')),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),
    )
