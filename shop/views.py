from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("index")
    return render(request,'shop/shop.html')
    
def about(request):
    return HttpResponse('about this page')

def contact(request):
    return HttpResponse('about this contact')    

def tracker(request):
    return HttpResponse('about this tracker')

def search(request):
    return HttpResponse('about this searchconcept')

def productview(request):
    return HttpResponse('about this productview')

def check(request):
    return HttpResponse('about this checkstatus')            
    
