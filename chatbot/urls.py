from django.urls import path
from chatbot import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    
]
