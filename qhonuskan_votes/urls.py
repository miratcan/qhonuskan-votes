from qhonuskan_votes.compat import re_path

from . import views

urlpatterns = [
    re_path(r'^vote/$', views.vote, name='qhonuskan_vote')
]
