

from django.conf.urls import url

from . import views

app_name = 'manager'
urlpatterns = [
url(r'^check_review_request', views.check_review_request, name='check_review_request'),
    url(r'^view_review_requests', views.view_review_requests, name='view_review_requests'),
    url(r'^view_employees', views.view_employees, name='view_employees'),
    url(r'^choose_evaluation_way', views.choose_evaluation_way, name='choose_evaluation_way'),
    url(r'^criterion_page', views.show_criterion_page, name='criterion_page'),
    url(r'^add_criterion', views.add_criterion, name='add_criterion'),
    url(r'^add_employees', views.add_employees_page, name='add_employees'),
    url(r'^criterion_page', views.show_criterion_page, name='criterion_page'),
    url(r'^add_criterion', views.add_criterion, name='add_criterion'),

    url(r'^edit_punish', views.edit_punish_page, name='edit_punish'),
    url(r'^add_punish', views.add_punish_page, name='add_punish'),
    url(r'^punish_page', views.show_punish_page, name='punish_page'),
    url(r'^employees_page', views.show_employees_page, name='employees_page'),
    url(r'^', views.show_manager_page, name='manager_first_page'),
]

