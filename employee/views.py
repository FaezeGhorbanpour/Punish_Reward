from django.shortcuts import render


# Create your views here.


def enter_var_values(request):
    return render(request, 'employee/enter_var_values.html')
def view_evaluations(request):
    return render(request, 'employee/view_evaluations.html')


def review_request(request):
    return render(request, 'employee/review_request.html')
def evaluation(request):
    return render(request, 'evaluator/evaluation.html')
def show_employee_page(request):
    return render(request, 'employee/employee.html')

