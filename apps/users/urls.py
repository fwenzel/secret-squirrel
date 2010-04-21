from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url('^$', views.display_profile, name='users.profile'),
    url('^edit/?$', views.edit_profile, name='users.edit'),
)
