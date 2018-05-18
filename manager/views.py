from django.shortcuts import render


# Create your views here.

def add_employee(request):
    return render(request, 'manager/add_employee.html')
def view_evaluator(request):
    return render(request, 'manager/view_evaluator.html')
def view_reevaluation_request(request):
    return render(request, 'manager/view_re-evaluation_request.html')
def choose_final_evaluation(request):
    return render(request, 'manager/choose_final_evaluation.html')
def view_employees(request):
    return render(request, 'manager/view_employees.html')

def add_evaluator(request):
    return render(request, 'manager/add_evaluator.html')

def choose_punish_reward(request):
    return render(request, 'manager/choose_punish_reward.html')
def view_criteria(request):
    return render(request, 'manager/view_criteria.html')

def show_manager_page(request):
    return render(request, 'manager/manager.html')


def show_criterion_page(request):
    return render(request, 'manager/criterion.html')


def add_criterion_page(request):
    return render(request, 'manager/add_criterion.html')


def edit_manager_page(request):
    return render(request, 'manager/edit_manager.html')


def show_each_request(request):
    return render(request, 'manager/each_request_page.html')


def show_request_page(request):
    return render(request, 'manager/review_request_page.html')