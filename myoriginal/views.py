from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'myoriginal/index.html')

def info(request):
    return render(request, 'myoriginal/info.html')
