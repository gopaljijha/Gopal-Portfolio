from django.contrib import admin
from django.conf.urls import url

from django.urls import path
from GopalPortfolio import views



# django admin changes
admin.site.site_header = "Login to Burhan"
admin.site.site_title = "Welocom to DashBord"
admin.site.index_title = "Welocom to Portal"



urlpatterns = [
    path('', views.home, name='PortfolioHome'),
    path('project', views.project, name='project'),
    path('#contact', views.contact, name='contact'),
    # path('skills', views.skills, name='skills'),
    # path('contact', views.contact, name='contact'),
]
