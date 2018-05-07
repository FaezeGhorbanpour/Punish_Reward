from django.conf.urls import url

from . import views

app_name = 'manager'
urlpatterns = [
    url(r'', views.show_manager_page, name='manager_first_page'),
    url(r'^criterion_page', views.show_criterion_page, name='criterion_page'),
    url(r'add_criterion', views.add_criterion_page, name='add_criterion'),
]
