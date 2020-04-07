from django.http import HttpResponse
from django.shortcuts import render

app_name = 'auth'
# Create your views here.
def index (request):
    return HttpResponse('oauth index');