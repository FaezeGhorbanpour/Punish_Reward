"""Punish_Reward URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', views.show_base_page, name='login'),
    path(r'master/', include('master.urls', namespace='master')),
    path(r'employee/', include('employee.urls', namespace='employee')),
    path(r'evaluator/', include('evaluator.urls', namespace='evaluator')),
    path(r'manager/', include('manager.urls', namespace='manager')),
    path(r'logout/', views.logout, name='logout')
]
