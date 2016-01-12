from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vote/$', views.vote, name='qhonuskan_vote')
]
