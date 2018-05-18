from django.conf.urls import url

from . import views

app_name = 'manager'
urlpatterns = [
    url(r'^add_employee', views.add_employee, name='add_employee'),

    url(r'^view_evaluator', views.view_evaluator, name='view_evaluator'),
    url(r'^view_re-evaluation_request', views.view_reevaluation_request, name='view_re-evaluation_request'),
    url(r'^choose_final_evaluation', views.choose_final_evaluation,name='choose_final_evaluation'),
    url(r'^view_employees', views.view_employees, name='view_employees'),
    url(r'^add_evaluator', views.add_evaluator, name='add_evaluator'),
    url(r'^choose_punish_reward', views.choose_punish_reward, name='choose_punish_reward'),
    url(r'^view_criteria', views.view_criteria, name='view_criteria'),
    url(r'^edit_manager', views.edit_manager_page, name='edit_manager'),
    url(r'^add_criterion', views.add_criterion_page, name='add_criterion'),
    url(r'^each_request', views.show_each_request, name='each_request'),
    url(r'^request_page', views.show_request_page, name='request_page'),
    url(r'^criterion_page', views.show_criterion_page, name='criterion_page'),
    url(r'^', views.show_manager_page, name='manager_first_page'),
]
