from django.conf.urls.defaults import *

from qhonuskan_votes import views

urlpatterns = patterns('',
    url(r'^vote/$', views.vote, name='vote'),
)
