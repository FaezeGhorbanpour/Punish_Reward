from django.conf.urls import url

from . import views

app_name = 'employee'
urlpatterns = [
    url(r'', views.show_employee_page, name='employee_first_page'),
    url(r'review', views.show_review_page, name='review_page')

]
