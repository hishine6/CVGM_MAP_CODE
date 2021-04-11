from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
from djangoProject.settings import GOOGLE_MAP_API_KEY


def index(request):
    return HttpResponse("Hello, World. You're at the lovely index.")

def show_map(request):
    context={'Key': GOOGLE_MAP_API_KEY  }
    return render(request, 'mapping.html',context )
