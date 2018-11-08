# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
# 用于序列化对象时querySet，如objects.all,objects.filter
from .models import Navi
# class Navi(models.Model):
#     name = models.CharField(verbose_name=u'名称', max_length=50)
#     description = models.CharField(verbose_name=u'描述', max_length=50)
#     url = models.URLField(verbose_name=u'URL')


# Create your views here.
def manage(request):
    # entries = serializers.serialize('json', Navi.objects.all())
    entries = Navi.objects.all()
    print(type(entries))
    return render(request, 'navi/manage.html', {'entries': entries})

