# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from navi.models import Navi
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    entries = Navi.objects.all()
    paginator = Paginator(entries, 5)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'pagination/pagination.html', {'contacts': contacts})




