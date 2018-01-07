# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __unicode__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default="匿名用户")
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.message