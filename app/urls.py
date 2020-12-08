# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # re_path(r'^.*\.html', views.pages, name='pages'),
    re_path(r'^.*member_table', views.pages, name='member_table'),
    # The home page
    path('', views.index, name='home'),
]
