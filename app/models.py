# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MemberInfo(models.Model):

    member = models.OneToOneField(User, on_delete=models.CASCADE)

    designation = models.CharField(max_length=60)
    district = models.CharField(max_length=60, blank=True)
    images = models.ImageField(upload_to='profilepics',blank=True)
    is_featured_member = models.BooleanField()
    is_home_featured_member=models.BooleanField()
    twitter_link: models.CharField(max_length=120, blank=True)
    fb_link: models.CharField(max_length=120, blank=True)\

    def __str__(self):

        return self.member.username
