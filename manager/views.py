
from django.shortcuts import render


# Create your views here.
def view_review_requests(request):
    return render(request, 'manager/view_review_requests.html')


def check_review_request(request):
    return render(request, 'manager/check_review_request.html')


def view_employees(request):
    return render(request, 'manager/view_employees.html')


def choose_evaluation_way(request):
    return render(request, 'manager/choose_evaluation_way.html')


def show_manager_page(request):
    return render(request, 'manager/manager.html')


def show_punish_page(request):
    return render(request, 'manager/punish.html')


def add_punish_page(request):
    return render(request, 'manager/add_punish.html')


def add_employees_page(request):
    return render(request, 'manager/add_employees.html')

def add_criterion(request):
    return render(request, 'manager/add_criterion.html')

def show_employees_page(request):
    return render(request, 'manager/show_employees.html')

def show_criterion_page(request):
    return render(request, 'manager/criterion.html')


def edit_punish_page(reqeust):
    return render(reqeust, 'manager/edit_punish.html')