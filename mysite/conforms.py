#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Wu Qiong
# Time: 2017/12/30 16:39

from django import forms

class ContactForm(forms.Form):
    CITY = [
        ['AQ', '安庆'],
        ['HZ', '杭州'],
        ['BJ', '北京'],
        ['SH', '上海'],
        ['HN', '海南'],
        ['HF', '合肥'],
    ]
    user_name = forms.CharField(label='你的姓名', max_length=20, initial='小明')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在校', required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='你的意见', widget=forms.Textarea(attrs={'col': '20', 'row': '3'}))