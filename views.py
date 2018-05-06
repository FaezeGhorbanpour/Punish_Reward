from django.http import HttpResponseRedirect
from django.shortcuts import render


def show_base_page(request):
    return render(request, 'login.html')


def show_manager_page(request):
    return render(request, 'manager/manager.html')


def logout(request):
    return HttpResponseRedirect('/')
