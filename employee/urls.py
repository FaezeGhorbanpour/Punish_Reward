from django.conf.urls import url

from . import views

app_name = 'employee'
urlpatterns = [
    url(r'^review_request', views.review_request, name='review_request'),
    url(r'^view_evaluations', views.view_evaluations, name='view_evaluations'),
    url(r'^enter_var_values', views.enter_var_values, name='enter_var_values'),
    url(r'^', views.show_employee_page, name='employee_first_page'),
]
