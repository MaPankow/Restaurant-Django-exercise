from django.urls import path

from menu import views

urlpatterns = [
    
    #path("", views.drinks_list, name="drinks"),
    #path("", views.starters_list, name="starters"),
    #path("", views.main_dishes_list, name="main_dishes"),
    path("", views.desserts_list, name="desserts"),
]