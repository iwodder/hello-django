from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('hello/index.html')
    context = {
            'msg': "Hello, world",
    }
    return HttpResponse(template.render(context, request))

def echo(request):
    res  = {"Message": "Hello, World"}
    return JsonResponse(res)

