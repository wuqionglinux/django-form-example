# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from mysite import models
from mysite import conforms
from mysite import postform
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.db.models.aggregates import Count


# Create your views here.
def index(request, pid=None, del_pass=None):
    template = get_template('index.html')
    # try:
    #     urid = request.GET['user_id']
    #     urpass = request.GET['user_pass']
    # except:
    #     urid = None
    # if urid != None and urpass == '12345':
    #     verified = True
    # else:
    #     verified = False
    # years = range(1960, 2021)
    # birthyear = request.GET['year']
    # favorcolors = request.GET.getlist('fcolor')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    # posts_num = models.Post.objects.aggregate(Count('pub_time'))
    # num = posts_num['pub_time__count'] % 3 # index中一行显示三个card，当一行不足三个card时，需要在循环的末尾再加上一个</div>
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = "每个字段都要填写"

    if user_id:
        try:
            mood = models.Mood.objects.get(status=user_mood)
        except:
            message = "没有该心情：{}，请重新选择！".format(user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, message=user_post, del_pass=user_pass)
        post.save()
        message = "成功存储，请牢记您的编辑密码：{}，信息审核通过后即可显示".format(user_pass)

    html = template.render(locals())
    return HttpResponse(html)


def post(request):
    template = get_template("post.html")
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        if not user_id or not user_pass or not user_post:
            message = "每个字段都要填写"
    except:
        user_id = None
        message = "每个字段都要填写"

    if user_id:
        try:
            mood = models.Mood.objects.get(status=user_mood)
        except:
            message = "没有该心情：{}，请重新选择！".format(user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, message=user_post, del_pass=user_pass)
        post.save()
        message = "成功存储，请牢记您的编辑密码：{}，信息审核通过后即可显示".format(user_pass)
    # request_context = RequestContext(request)
    # request_context.push(locals())
    html = template.render(locals(), request)
    return HttpResponse(html)


def list(request, pid=None, del_pass=None):
    template = get_template('list.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    if pid and del_pass:
        try:
            post = models.Post.objects.get(id=pid)
            if del_pass == post.del_pass:
                post.delete()
                message = "成功删除{}的留言！".format(post.nickname)
            else:
                message = "密码不正确，请重新输入【{}】删帖密码！".format(post.nickname)
        except:
            message = "没有该ID！"
    html = template.render(locals())
    return HttpResponse(html)


def contact(request):
    if request.method == "POST":
        form = conforms.ContactForm(request.POST)
        if form.is_valid():
            message = "感谢你的反馈！"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            mail_body = u"""
            网友姓名：{}
            居住城市：{}
            是否在学：{}
            反映意见：{}""".format(user_name, user_city, user_school, user_message)
            email = EmailMessage('来自【NBA球员留言板】网站的网友意见', mail_body, user_email, ['252792836@qq.com'])
            email.send()
        else:
            message = "输入信息有误，请检查！"
    else:
        form = conforms.ContactForm()
    template = get_template('contact.html')
    html = template.render(locals(), request)
    return HttpResponse(html)


def post2db(request):
    template = get_template('post2db.html')
    if request.method == "POST":
        post2dbform = postform.PostForm(request.POST)
        if post2dbform.is_valid():
            post2dbform.save()
            message = "成功存储，请牢记您的编辑密码：{}，信息审核通过后即可显示".format(request.POST['del_pass'])
            return HttpResponseRedirect('/list')
    else:
        post2dbform = postform.PostForm()
        message = "每个字段都要填写"
    html = template.render(locals(), request)
    return HttpResponse(html)
