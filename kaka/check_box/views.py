# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def cb_index(request):
    return render(request, 'check_box/index.html')




