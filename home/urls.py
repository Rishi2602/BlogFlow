from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name='index'),
    path('delete/<int:del_id>', views.delete, name='delete'),
    path('update/<int:del_id>', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('', views.login_page, name='login_page'),
    path('logout/', views.logoutUser, name='logout'),
    path('add/', views.add, name='add'),
    path('CompletedList/', views.colist, name='colist'),
    path('profile/', views.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)