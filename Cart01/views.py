from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from Cart01.models import shopProduct

from .forms import NameForm

# Create your views here.

def home(request):
    
    return render(request,"home.html")

def about(request):
    
    return render(request,"about.html")

def contact(request):
    
    return render(request,"contact.html")

def blog(request):
    
    return render(request,"blog.html")

def shop(request):
    
    itms = shopProduct.objects.all()
    q = {"itms": itms}
#    key:value pair
    return render(request,"shop.html",q)



def login(request):
    if request.method =='POST':
        form =NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request,'name.html',{'form':form})

def userLog_in(request):
    context={}
    return render(request,"userLog_in.html",context)