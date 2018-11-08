# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys

reload(sys)
sys.setdefaultencoding('utf8')


# Create your models here.
class Navi(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=50)
    description = models.CharField(verbose_name=u'描述', max_length=50)
    url = models.URLField(verbose_name=u'URL')

    def __str__(self):
        return self.name

