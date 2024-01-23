from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]