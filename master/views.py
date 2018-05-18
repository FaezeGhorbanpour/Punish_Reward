from django.shortcuts import render


# Create your views here.
def view_review_requests(request):
    return render(request, 'master/view_review_requests.html')


def check_review_request(request):
    return render(request, 'master/check_review_request.html')


def view_employees(request):
    return render(request, 'master/view_employees.html')


def choose_evaluation_way(request):
    return render(request, 'master/choose_evaluation_way.html')


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