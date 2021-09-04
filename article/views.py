from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def rent(request):
    return render(request,"rent.html")


def Ozkan(request):
    return render(request,"ozkan.html")

def Ozkan1(request):
    return render(request,"ozkan1.html")

def Ozkan2(request):
    return render(request,"ozkan2.html")


