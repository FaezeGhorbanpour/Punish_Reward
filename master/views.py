from django.shortcuts import render


# Create your views here.


def show_master_page(request):
    return render(request, 'master/master.html')


def show_punish_page(request):
    return render(request, 'master/punish.html')
