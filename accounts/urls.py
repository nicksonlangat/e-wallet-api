from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

router = DefaultRouter()
router.register(r"register", views.SignUpUserView, basename="register_user")
router.register(r"users", views.UserListView, basename="all_users")

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login_user"),
    path("refresh/token/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
