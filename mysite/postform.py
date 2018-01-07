#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Wu Qiong
# Time: 2017/12/31 13:27
from django import forms
from mysite import models
from captcha.fields import CaptchaField
class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'message', 'nickname', 'del_pass']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '现在的心情'
        self.fields['message'].label = '留言板'
        self.fields['nickname'].label = '你的昵称'
        self.fields['del_pass'].label = '设置删帖密码'
        self.fields['captcha'].label = '请输入验证码'
