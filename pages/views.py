from django.shortcuts import render
from django.http import HttpResponse

# Controller, Router

# Create your views here.
def index(request):
  return render(request,'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')