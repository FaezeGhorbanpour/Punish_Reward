from django.shortcuts import render


# Create your views here.


def enter_var_values(request):
    return render(request, 'evaluator/enter_var_values.html')
def view_employees(request):
    return render(request, 'evaluator/view_employees.html')
def check_reevaluation_request(request):
    return render(request, 'evaluator/check_re-evaluation_request.html')
def evaluation(request):
    return render(request, 'evaluator/evaluation.html')
def show_employee_page(request):
    return render(request, 'evaluator/evaluator.html')

