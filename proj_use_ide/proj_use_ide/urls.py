"""proj_use_ide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import views


handler500 = 'proj_use_ide.views.page_500'
handler404 = 'proj_use_ide.views.page_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    #重定向
    path('index1/', views.index_one, name='index_one'),
    path('index2/', views.index_two, name='index_two'),


    re_path('time/$', views.new_time),
    re_path('now/$', views.new_now),
    re_path('article/(?P<year>\d+)/', views.article),

    path('auth/', include('oauth.urls')),

    path('error/', views.error_page),



]

urlpatterns += [re_path('medias/(?P<path>.*)', serve, {
        'document_root': settings.MEDIA_ROOT
    }),]