"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path as url
from AuthenticationApp.views import signup, signin, signout, signoutHome, activate
from SignupApp.views import signup_action
from LoginApp.views import login_action
# from GopalPortfolio.views import portfolioHome, portfolioAbout, portfolioSkills, portfolioResume, portfolioContactUs, portfolioProjects
# from BasicApp import views 

from GopalPortfolio import views
from BasicApp.views import blog_view, about_view, contact_view 


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index, name="basic"),
    # path('', views.home_view),
    # path('', views.logo_view),
    # path('basic/about', views.about_view, name="about"),
    # path('basic/blog', views.blog_view, name="blog"),
    # path('basic/contact', views.contact_view, name="contact"),
    # path('basic/news', views.news_view, name="news"),
    # path('basic/product', views.product_view, name="product"),
    # path('GopalPortfolio/PortfolioClick', views.portfolio_click, name="portfolio"),

    # # Portfolio
    # path('GopalPortfolio/portfolioHome', portfolioHome, name="portfolioHome"),
    # path('GopalPortfolio/PortfolioAbout', portfolioAbout, name="portfolioAbout"),
    # path('GopalPortfolio/portfolioSkills', portfolioSkills, name="portfolioSkills"),
    # path('GopalPortfolio/portfolioProjects', portfolioProjects, name="portfolioProjects"),
    # path('GopalPortfolio/portfolioResume', portfolioResume, name="portfolioResume"),
    # path('GopalPortfolio/portfolioContactUs', portfolioContactUs, name="portfolioContactUs"),

   path('admin/', admin.site.urls),
    path('', views.portfolioHome, name="GopalPortfolio"),
    # path('', views.home_view),
    # path('', views.logo_view),
    path('basic/about', about_view, name="about"),
    path('basic/blog', blog_view, name="blog"),
    path('basic/contact', contact_view, name="contact"),
    # path('basic/news', views.news_view, name="news"),
    # path('basic/product', views.product_view, name="product"),
    # path('GopalPortfolio/PortfolioClick', views.portfolio_click, name="portfolio"),

    # Portfolio
    path('GopalPortfolio/portfolioHome', views.portfolioHome, name="portfolioHome"),
    path('GopalPortfolio/PortfolioAbout', views.portfolioAbout, name="portfolioAbout"),
    path('GopalPortfolio/portfolioSkills', views.portfolioSkills, name="portfolioSkills"),
    path('GopalPortfolio/portfolioProjects', views.portfolioProjects, name="portfolioProjects"),
    path('GopalPortfolio/portfolioResume', views.portfolioResume, name="portfolioResume"),
    path('GopalPortfolio/portfolioContactUs', views.portfolioContactUs, name="portfolioContactUs"),
  
   
]
