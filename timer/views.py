from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

# Create your views here.
def timer (request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'title': 'Egg Timer'}, request))

def runny (request):
    template = loader.get_template('runny.html')
    return HttpResponse(template.render({'title': 'Runny Yolk'}, request))

def soft (request):
    template = loader.get_template('soft.html')
    return HttpResponse(template.render({'title': 'Soft Boiled'}, request))

def hard (request):
    template = loader.get_template('hard.html')
    return HttpResponse(template.render({'title': 'Hard Boiled'}, request))

def over (request):
    template = loader.get_template('over.html')
    return HttpResponse(template.render({'title': 'Over Cooked'}, request))
