import django
from django.db import models
from django.shortcuts import render, HttpResponse

# Create your views here.
def portfolioHome(request):
    return render(request, 'GopalPortfolio/PortfolioHome.html')


def portfolioAbout(request):
    return render(request, 'GopalPortfolio/PortfolioAbout.html')

def portfolioResume(request):
    return render(request, 'GopalPortfolio/PortfolioResume.html')

def portfolioSkills(request):
    return render(request, 'GopalPortfolio/PortfolioSkills.html')

def portfolioProjects(request):
    return render(request, 'GopalPortfolio/PortfolioProjects.html')

# def portfolioResume(request):
#     return render(request, 'GopalPortfolio/PortfolioResume.html')

def portfolioContactUs(request):
    return render(request, 'GopalPortfolio/PortfolioContactUS.html')

def contact(request):
    return render(request, 'PortfolioHome.html')

