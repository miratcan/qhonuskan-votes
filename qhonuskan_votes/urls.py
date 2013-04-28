from qhonuskan_votes import views
from qhonuskan_votes.compat import patterns, url

urlpatterns = patterns(
    '',

    url(r'^vote/$', views.vote, name='vote'),
)
