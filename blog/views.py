

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("index blog")
    return render(request,'blog/blog.html')

