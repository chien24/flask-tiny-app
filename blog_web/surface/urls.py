from django.urls import path
from . import views

app_name = 'surface'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('home/logout/', views.logout_action, name='logout'),
]