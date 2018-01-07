# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('mood', 'nickname', 'del_pass', 'pub_time', 'enabled')
    ordering = ('-pub_time',)

admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)