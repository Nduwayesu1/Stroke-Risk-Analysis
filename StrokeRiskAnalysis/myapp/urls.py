from django.urls import path
from django.contrib import admin  # Fix the import
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Correct admin import
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # Login page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('users/', views.user_list, name='user_list'),
    path('StrokePrdedectionDashboard/', views.predict, name='StrokePrdedectionDashboard'),  # Dashboard
]
