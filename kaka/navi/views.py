# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
# from django.core import serializers
# 用于序列化对象时querySet，如objects.all,objects.filter
from .models import Navi
# class Navi(models.Model):
#     name = models.CharField(verbose_name=u'名称', max_length=50)
#     description = models.CharField(verbose_name=u'描述', max_length=50)
#     url = models.URLField(verbose_name=u'URL')


# Create your views here.
def manage(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        description = request.POST.get('description')
        urlname = request.POST.get('urlname')
        # print(firstname, description, urlname)
        if firstname and description and urlname:
            ft = Navi.objects.filter(name=firstname)
            if ft:
                ret = {'status': '1', 'msg': '名称已经存在'}
            else:
                Navi.objects.create(name=firstname, description=description, url=urlname)
                ret = {'status': 0}
        else:
            ret = {'status': '1', 'msg': '输入不能为空'}

        return HttpResponse(json.dumps(ret))

    # entries = serializers.serialize('json', Navi.objects.all())
    entries = Navi.objects.all()
    # print(type(entries))
    return render(request, 'navi/manage.html', {'entries': entries})


def edit(request):
    filter_name = request.POST.get('mod_name')
    modify_infos = Navi.objects.get(name=filter_name)
    name = modify_infos.name
    des = modify_infos.description
    url = modify_infos.url
    ret = {'name': name, 'des': des, 'url': url}

    return HttpResponse(json.dumps(ret))


def modify(request):
    if request.method == 'POST':
        m_name = request.POST.get('m_name')
        name = request.POST.get('firstname')
        des = request.POST.get('description')
        url = request.POST.get('urlname')
        # print('x:{},y:{},z:{},t:{}'.format(m_name, name, des, url))

        # # check_name = Navi.objects.filter(name=name)
        # check_name = ''
        # if check_name:
        #     ret = {'status': 1, 'msg': '名称已存在'}
        #     return HttpResponse(json.dumps(ret))

        try:
            Navi.objects.filter(name=m_name).update(name=name, description=des, url=url)
            ret = {'status': 0}
        except Exception as e:
            print('ERROR:{}'.format(e))
            ret = {'status': 1, 'msg': '名称不能重复'}

        return HttpResponse(json.dumps(ret))


def delete(request):
    if request.method == 'POST':
        name_str = request.POST.get('name_str')
        print(name_str.split(','))
        for name in name_str.split(','):
            print(name)
            Navi.objects.filter(name=name).delete()

        ret = {'status': 0, 'msg': '删除成功'}

        return HttpResponse(json.dumps(ret))










