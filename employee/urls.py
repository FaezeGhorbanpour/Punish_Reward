from django.conf.urls import url

from . import views

app_name = 'employee'
urlpatterns = [
    url(r'^edit_employee', views.edit_employee_page, name='edit_employee'),
    url(r'^review', views.show_review_page, name='review_page'),
    url(r'^', views.show_employee_page, name='employee_first_page'),
]
