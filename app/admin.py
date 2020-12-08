# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from app.models import MemberInfo
from django.contrib import admin
from app.views import pages
admin.site.register(MemberInfo)

# Register your models here.
