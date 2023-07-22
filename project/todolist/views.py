from django.shortcuts import render, redirect
from django.contrib import messages
 
# import todo form and models
 
from .forms import TodoForm
from .models import Todo
 
###############################################
 
# Header link

def index(request):
    return render(request, 'basic/index.html')

def logo_view(request):
    return render(request, 'basic/index.html')

def home_view(request):
    return render(request,'basic/home.html')

# def about_view(request):
#     return render(request,'todolist/about.html')

def product_view(request):
    return render(request, 'basic/product.html')

def news_view(request):
    return render(request, 'basic/news.html')

def technology_view(request):
    return render(request, 'basic/technology.html')


def about_view(request):
    return render(request,'basic/about.html')


   







# Footer Link
def blog_view(request):
    return render(request,'basic/blog.html')

def contact_view(request):
    return render(request,'basic/contact.html')

# Create your views here.
