from django.shortcuts import render


# Create your views here.


def show_manager_page(request):
    return render(request, 'manager/manager.html')


def show_criterion_page(request):
    return render(request, 'manager/criterion.html')


def add_criterion_page(request):
    return render(request, 'manager/add_criterion.html')
