from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main_page, name='main_page'),
    path('registration/', views.registration, name='registration'),
    path('autharization/', views.autharization, name='autharization'),
    path('logout/', views.user_logout, name='logout'),
    path('cabinet/', views.go_to_cabinet, name='cabinet'),
    path('create_calltouch/', views.create_calltouch, name='create_calltouch')
]
