from django.shortcuts import render


# Create your views here.


def show_master_page(request):
    return render(request, 'master/master.html')


def show_punish_page(request):
    return render(request, 'master/punish.html')


def add_punish_page(request):
    return render(request, 'master/add_punish.html')


def add_employees_page(request):
    return render(request, 'master/add_employees.html')

def add_criterion(request):
    return render(request, 'master/add_criterion.html')

def show_employees_page(request):
    return render(request, 'master/show_employees.html')

def show_criterion_page(request):
    return render(request, 'master/criterion.html')


def edit_punish_page(reqeust):
    return render(reqeust, 'master/edit_punish.html')