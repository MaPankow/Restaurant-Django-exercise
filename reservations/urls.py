from django.urls import path
from . import views

urlpatterns = [
    path("", views.reserve_table, name="reservation"),
    path("guests/", views.view_reservations, name="guests"),
]