from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from project import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


# Header link
def index(request):
    return render(request, 'basic/index.html')

def logo_view(request):
    return render(request, 'basic/index.html')

def home_view(request):
    return render(request,'basic/home.html')

def product_view(request):
    return render(request, 'basic/product.html')

def news_view(request):
    return render(request, 'basic/news.html')


# On click portfolio directly About
def portfolio_click(request):
    return render(request, 'GopalPortfolio/PortfolioAbout.html')


def about_view(request):
    return render(request,'basic/about.html')

# Footer Link
def blog_view(request):
    return render(request,'basic/blog.html')

def contact_view(request):
    return render(request,'basic/contact.html')

# Create your views here.
