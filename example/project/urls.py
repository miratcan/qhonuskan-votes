from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^votes/', include('qhonuskan_votes.urls')),
)
