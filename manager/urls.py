from django.conf.urls import url

from . import views

app_name = 'manager'
urlpatterns = [
    url(r'^edit_manager', views.edit_manager_page, name='edit_manager'),
    url(r'^add_criterion', views.add_criterion_page, name='add_criterion'),
    url(r'^criterion_page', views.show_criterion_page, name='criterion_page'),
    url(r'^', views.show_manager_page, name='manager_first_page'),
]
