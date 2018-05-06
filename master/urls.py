from django.conf.urls import url

from . import views

app_name = 'master'
urlpatterns = [
    url(r'^', views.show_master_page, name='master_first_page'),
    url(r'punish_page', views.show_punish_page, name='punish_page')
]
