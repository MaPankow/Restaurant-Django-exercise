from django.urls import path
from .views import MenuItemList
from menu import views

urlpatterns = [
    
    #path("", views.drinks_list, name="drinks"),
    #path("", views.starters_list, name="starters"),
    #path("", views.main_dishes_list, name="main_dishes"),
    path("", views.menu_list, name="menu"),
    path('api/', MenuItemList.as_view(), name='menu-list'),
]