from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add/', views.add_post, name='add_post'),
]