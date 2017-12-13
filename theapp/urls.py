"""lab8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #register page
    url(r'^register/$', views.registerUser, name='registerUser'),
    # login page
    url(r'^login/$', views.login, name='login'),
    # logout page
    url(r'^logout/$', views.logout, name='logout'),
    # Ajax: check if user exists on login page
    url(r'^logcheckuser/$', views.logCheckUser, name='logCheckUser'),
    url(r'^checkpassword/$', views.checkpassword, name='logout'),
    
    url(r'^news/$', views.news),
    url(r'^(?i)news/sp', views.sport),
    url(r'^(?i)news/bs', views.business),
    url(r'^news/(?P<article_id>[0-9]+)/$', views.article),
    url(r'^postcomment/(?P<article_id>[0-9]+)/$', views.postComment),
    url(r'^profile/$', views.profile, name='profile'),
    

]
