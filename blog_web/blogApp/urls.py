from django.urls import path

from . import views


app_name = 'blogApp'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/delete/', views.deletePost, name='delete'),
    path('<int:post_id>/update/', views.updatePost, name='update'),
    path('deletelistpost/', views.deleteListPost, name='delete-list-posts'),
    
]