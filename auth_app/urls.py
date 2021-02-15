from django.urls import path
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.show_main_page, name='main_page'),
    path('registration/', views.registration, name='registration'),
    path('autharization/', views.autharization, name='autharization'),
    path('logout/', views.user_logout, name='logout'),
    path('cabinet/', views.go_to_cabinet, name='cabinet'),
    path('cabinet/create_calltouch/', views.create_calltouch, name='create_calltouch'),
    path('cabinet/new_calltouch_created/', views.validate_calltouch, name='new_calltouch_created'),
    path('cabinet/my_connections/', views.my_connections, name='my_connections'),
    path('cabinet/links_input_form/', views.links_input_form, name='links_input_form'),
    path('cabinet/links_sent/', views.send_links_to_check, name='links_sent'),
    path('cabinet/links_result/', views.links_result, name='links_result'),
]
