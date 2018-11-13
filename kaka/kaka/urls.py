"""kaka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from kaka_app1 import views as app1_views
from navi import views as navi_views
from check_box import views as cb_views
from pagination import views as pg_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app1_views.index, name='index'),
    url(r'^manage/', navi_views.manage, name='manage'),
    url(r'^edit/', navi_views.edit, name='edit'),
    url(r'^modify/', navi_views.modify, name='modify'),
    url(r'^checkbox/', cb_views.cb_index, name='checkbox'),
    url(r'^delete/', navi_views.delete, name='delete'),
    url(r'^pagination', pg_views.index, name='pagination'),
]
