# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Content(models.Model):
    content = models.CharField(max_length=100, verbose_name='内容项')
    remarks = models.CharField(max_length=100, verbose_name='备注')
    content_status = models.CharField(max_length=10, verbose_name='状态')
    content_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')













