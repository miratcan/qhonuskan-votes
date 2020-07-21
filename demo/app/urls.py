from django.contrib import admin
from qhonuskan_votes.compat import include, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^votes/', include('qhonuskan_votes.urls')),
]
