# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.core import serializers

from models import Content

import time, json

"""
content = models.CharField(max_length=100, verbose_name='内容项')
remarks = models.CharField(max_length=100, verbose_name='备注')
content_status = models.CharField(max_length=10, verbose_name='状态')
content_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
"""


# Create your views here.
def index(request):
    ctx = {'title': 'Index'}
    ctts = Content.objects.all()
    ctx['ctts'] = ctts
    return render(request, 'index.html', context=ctx)


def add(request):
    if request.method == 'POST':
        content = request.POST.get('sub_content')
        remark = request.POST.get('sub_remark')
        content_status = '进行中'
        content_time = time.strftime('%Y-%m-%d')
        print(content, remark, content_status, content_time)
        Content.objects.create(content=content, remarks=remark, content_status=content_status, content_time=content_time)
        ret = {'status': 0}

        return HttpResponse(json.dumps(ret))


def check_job(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        jobs = serializers.serialize('json', Content.objects.filter(content_status=choice))
        if json.loads(jobs):
            ret = {'status': 0, 'jobs': jobs}
            print(ret)
            return HttpResponse(json.dumps(ret))

        ret = {'status': 1, 'jobs': '无数据'}
        return HttpResponse(json.dumps(ret))


