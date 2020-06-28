from django import VERSION as DJANGO_VERSION

if DJANGO_VERSION >= (2, 0):
    from django.urls import *
else:
    from django.conf.urls import url as re_path, include
    from django.contrib.auth import get_user_model

    User = get_user_model()
