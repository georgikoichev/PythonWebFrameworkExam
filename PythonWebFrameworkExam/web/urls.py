from django.urls import path
from PythonWebFrameworkExam.web import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard_page, name='dashboard'),
    path('details/<int:pk>/', views.thread_details, name='thread_details'),
    path('create', views.create_thread, name='create_thread'),
    path('edit/<int:pk>/', views.edit_thread, name='edit_thread'),
    path('delete/<int:pk>/', views.delete_thread, name='delete_thread'),
    path('calculator', views.calculator_page, name='calculator'),
    path('functions', views.functions_page, name='functions'),
]