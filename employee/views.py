from django.shortcuts import render


# Create your views here.


def show_employee_page(request):
    return render(request, 'employee/employee.html')
