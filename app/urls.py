from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration", views.registration, name="registration"),
    path("login", views.user_login, name="login"),
    path("user-logout", views.user_logout, name="user_logout"),
]


handler404 = "app.views.error_404_view"
