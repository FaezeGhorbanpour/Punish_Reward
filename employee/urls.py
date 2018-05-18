from django.conf.urls import url

from . import views

app_name = 'employee'
urlpatterns = [
    url(r'^view_employees', views.view_employees, name='view_employees'),
    url(r'^enter_var_values', views.enter_var_values, name='enter_var_values'),
    url(r'^check_re-evaluation_request', views.check_reevaluation_request, name='check_re-evaluation_request'),
    url(r'^evaluation', views.evaluation, name='evaluation'),
    url(r'^', views.show_employee_page, name='employee_first_page'),
]
