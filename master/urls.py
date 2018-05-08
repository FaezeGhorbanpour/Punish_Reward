from django.conf.urls import url

from . import views

app_name = 'master'
urlpatterns = [
    url(r'^add_employees', views.add_employees_page, name='add_employees'),
    url(r'^add_punish', views.add_punish_page, name='add_punish'),
    url(r'^punish_page', views.show_punish_page, name='punish_page'),
    url(r'^employees_page', views.show_employees_page, name='employees_page'),
    url(r'^', views.show_master_page, name='master_first_page'),
]
