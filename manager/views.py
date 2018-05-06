from django.shortcuts import render


# Create your views here.


def show_manager_page(request):
    return render(request, 'manager/manager.html')
