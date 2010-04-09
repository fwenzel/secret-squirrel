from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    # The homepage.
    url('^$', direct_to_template, {'template': 'sso/home.html'},
        name='home'),
)
