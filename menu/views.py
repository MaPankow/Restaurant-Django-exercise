from django.shortcuts import render
#from django.views.generic import TemplateView
from .models import MenuItem, MenuCategory
from rest_framework import viewsets
from .serializers import MenuItemSerializer, MenuCategorySerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
# Create your views here.

# class MenuView(TemplateView):
#     template_name = "menu/menu.html"

def menu_list(request):
    #menu_list = MenuItem.objects.all()
    menu_categories = MenuCategory.objects.all()
    context = {
        'menu_categories': menu_categories
    }
    return render(request, 'menu/menu.html', context)

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer