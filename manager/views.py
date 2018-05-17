from django.shortcuts import render


# Create your views here.


def show_manager_page(request):
    return render(request, 'manager/manager.html')


def show_criterion_page(request):
    return render(request, 'manager/../templates/master/criterion.html')


def add_criterion_page(request):
    return render(request, 'manager/../templates/master/add_criterion.html')


def edit_manager_page(request):
    return render(request, 'manager/edit_manager.html')


def show_each_request(request):
    return render(request, 'manager/each_request_page.html')


def show_request_page(request):
    return render(request, 'manager/review_request_page.html')