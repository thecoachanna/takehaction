from django.urls import path, include
from . import views

urlpatterns = [
    # Welcome / landing page
    path("", views.index, name="index"),
    # Django built-in login system
    path("accounts/", include("django.contrib.auth.urls")),
    path("create_user", views.create_user, name="create_user"),
    # User profile
    path("profile", views.profile, name="profile"),
    # General information
    path("info", views.info, name="info"),
]
