from django.urls import path
from .views import register, lougout_view, CustomLoginView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", lougout_view, name="logout"),
]
