from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hit/',views.index,name="shophome"),
    path('about/',views.about,name="aboutus"),
    path('contact/',views.contact,name="contactus"),
    path('tracker/',views.tracker,name="trackingstatus"),
    path('search/',views.search,name="search"),
    path('productview/',views.productview,name="products"),
    path('checkout/',views.check,name='checktype'),
    
]
