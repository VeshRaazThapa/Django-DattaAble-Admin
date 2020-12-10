# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
##todo: fb link and twitter link not working


# Create your models here.

class MemberInfo(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60, default="")
    middle_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60,default="")
    email = models.EmailField(blank=True, null=True,default="")
    designation = models.CharField(max_length=60)
    district = models.CharField(max_length=60, blank=True, null=True)
    profile_link_twt = models.URLField(null=True, blank=True)
    profile_link_fb = models.URLField(null=True, blank=True,)
    image = models.ImageField(upload_to='profilepics', blank=True, null=True)
    is_featured_member = models.BooleanField()
    is_home_featured_member = models.BooleanField()

    def __str__(self):

        return self.member_id
