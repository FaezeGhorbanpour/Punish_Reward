from django.shortcuts import render


# Create your views here.

def add_employee(request):
    return render(request, 'master/add_employee.html')
def view_evaluator(request):
    return render(request, 'master/view_evaluator.html')
def view_reevaluation_request(request):
    return render(request, 'master/view_re-evaluation_request.html')
def choose_final_evaluation(request):
    return render(request, 'master/choose_final_evaluation.html')
def view_employees(request):
    return render(request, 'master/view_employees.html')

def add_evaluator(request):
    return render(request, 'master/add_evaluator.html')

def choose_punish_reward(request):
    return render(request, 'master/choose_punish_reward.html')
def view_criteria(request):
    return render(request, 'master/view_criteria.html')

def show_master_page(request):
    return render(request, 'master/master.html')


def show_criterion_page(request):
    return render(request, 'master/criterion.html')


def add_criterion_page(request):
    return render(request, 'master/add_criterion.html')


def edit_master_page(request):
    return render(request, 'master/edit_master.html')


def show_each_request(request):
    return render(request, 'master/each_request_page.html')


def show_request_page(request):
    return render(request, 'master/review_request_page.html')
