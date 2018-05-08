from django.shortcuts import render


# Create your views here.


def show_employee_page(request):
    return render(request, 'employee/employee.html')


def show_review_page(request):
    return render(request, 'employee/review.html')


def edit_employee_page(request):
    return render(request, 'employee/edit_employee.html')
