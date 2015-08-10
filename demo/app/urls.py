from django.contrib import admin
from qhonuskan_votes.compat import patterns, include, url

admin.autodiscover()

urlpatterns = patterns(
    'app.views',

    url(r'^$', 'home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^votes/', include('qhonuskan_votes.urls')),
)
