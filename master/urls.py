from django.conf.urls import url

from . import views

app_name = 'master'
urlpatterns = [
    url(r'^add_employees', views.add_employees_page, name='add_employees'),
    url(r'^criterion_page', views.show_criterion_page, name='criterion_page'),
    url(r'^add_criterion', views.add_criterion, name='add_criterion'),

    url(r'^edit_punish', views.edit_punish_page, name='edit_punish'),
    url(r'^add_punish', views.add_punish_page, name='add_punish'),
    url(r'^punish_page', views.show_punish_page, name='punish_page'),
    url(r'^employees_page', views.show_employees_page, name='employees_page'),
    url(r'^', views.show_master_page, name='master_first_page'),
]
