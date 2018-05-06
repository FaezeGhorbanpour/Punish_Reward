from django.conf.urls import url

from . import views

app_name = 'manager'
urlpatterns = [
    url(r'', views.show_manager_page, name='manager_first_page')
]
