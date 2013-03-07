from django.conf.urls import *

from qhonuskan_votes import views

urlpatterns = patterns('',
    url(r'^vote/$', views.vote, name='vote'),
)
