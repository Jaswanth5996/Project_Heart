from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("login", views.LoginView, name="login"),
    path("logout", views.Logout, name="logout"),
    path("messages", views.Message, name="messages"),
]
