from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import product
from math import ceil
# Create your views here.
def index(request):
    #return HttpResponse("index")
    products=product.objects.all()
    print(products)
    #n=len(products)
    #nslides=n//4+ceil((n/4)-(n//4))
   # params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
   # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])
    params={'allprods':allprods}
    return render(request,'shop/shop.html',params)
    
def about(request):
    return render(request,'shop/about.html')

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


