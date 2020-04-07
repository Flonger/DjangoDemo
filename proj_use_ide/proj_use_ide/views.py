import os
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import loader
from django.urls import reverse



def index (request):

    return HttpResponse('OK')


def index_one (request):
    # return HttpResponse('index one'),

    #重定向到two
    # return HttpResponseRedirect('/index2')
    # return redirect('/index2')

    # url = reverse('index_two')
    # return redirect(url)

    return redirect('index_two')

def index_two (request):
    return HttpResponse('index two')



def article (request, year):
    #获取url中的参数
    print('year: {0}'.format(year))
    #获取GET参数
    month = request.GET.get('month',None)
    print('month: {0}'.format(month))
    return HttpResponse('article:' + year)

def new_time (request):
     # 展示系统当前时间
     now = datetime.now()
     html = """
        <html>
            <head>
                <style type="text/css">
                    body{{color:red;}}
                </style>
            </head>
            <body>
            now : {0}
            </body>
        </html>
     """.format(now)
     return HttpResponse(html)

def new_now (request):
    #从html文件读取并响应
    html = ''
    now = datetime.now()
    #使用文件读取
    # file_name = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    # with open(file_name) as f:
    #     html = f.read()
    # return HttpResponse(html)

    #使用django方法
    # templ = loader.get_template('index.html')
    # html = templ.render({
    #     'now':now
    # })
    # return HttpResponse(html)

    #使用render
    # return render(request,'index.html',{
    #     'now': now
    # })

    return render_to_response('index.html',{
        'now': now
    })


def page_500(request):
    return HttpResponse('服务器正忙')


def page_404(request, exception):
    return HttpResponse('资源丢失')


def error_page(request):
    #产生500
    raise ValueError

    return HttpResponse()