from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add/', views.add_post, name='add_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.update_post, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
]