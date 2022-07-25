from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('delete/<int:del_id>', views.delete, name='delete'),
    path('update/<int:del_id>', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('', views.login_page, name='login_page'),
    # path('info/', views.info, name='info'),
    path('logout/', views.logoutUser, name='logout'),
    path('add/', views.add, name='add'),
    path('CompletedList/', views.colist, name='colist')
]
