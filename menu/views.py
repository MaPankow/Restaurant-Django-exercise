from django.shortcuts import render
#from django.views.generic import TemplateView
from .models import MenuItem, MenuCategory
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

