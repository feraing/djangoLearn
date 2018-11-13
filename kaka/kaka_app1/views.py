# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from navi.models import Navi


# Create your views here.
def index(request):
    entries = Navi.objects.all()
    return render(request, 'index.html', {'entries': entries})

