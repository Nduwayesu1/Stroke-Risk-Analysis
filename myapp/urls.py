from django.urls import path
from django.contrib import admin  # Import the admin module
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Only include admin URLs once
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # Login page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('users/', views.user_list, name='user_list'),
    path('StrokePredictionDashboard/', views.predict, name='StrokePredictionDashboard'),  # Fixed typo
]
