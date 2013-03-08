try:
    # For django 1.5+
    from django.conf.urls import *
except:
    # For django 1.4.5 and lower
    from django.conf.urls.defaults import *

from qhonuskan_votes import views

urlpatterns = patterns('',
    url(r'^vote/$', views.vote, name='vote'),
)
