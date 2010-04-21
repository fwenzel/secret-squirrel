from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    ('', include('sso.urls')),

    # order is important here: Both apps provide login/logout so only the
    # first will match.
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
