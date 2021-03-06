"""App01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cart01.views import home, contact, about, blog, shop, login, userLog_in
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='Home Page'),
    path('home/',home,name='Home Page'),
    path('contact/',contact,name='Contact Page'),
    path('about/',about,name='About Page'),
    path('blog/',blog,name='Home Page'),
    path('shop/',shop,name='Shopping Page'),
    path('signup/',login,name='Sign Up Page'),
    path('userlogin/',userLog_in,name='Sign Up Page2'),
    
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
