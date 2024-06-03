from django.urls import path
from .views import AboutPageView, HomePageView, ContactPageView, MenuPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutPageView.as_view(), name="about"),
    path("menu", MenuPageView.as_view(), name="menu"),
    path("contact", ContactPageView.as_view(), name="contact"),
]   