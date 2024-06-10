from django.shortcuts import render
#from django.views.generic import TemplateView
from .models import MenuItem, MenuCategory
# Create your views here.

# class MenuView(TemplateView):
#     template_name = "menu/menu.html"

def drinks_list(request):
    #menu_list = MenuItem.objects.all()
    drinks_list = MenuItem.objects.filter(catgory_id=1).values()
    context = {
        'drinks_list': drinks_list
    }
    return render(request, 'menu/menu.html', context)

def starters_list(request):
    
    starters_list = MenuItem.objects.filter(catgory_id=3).values()
    context = {
        'starters_list': starters_list
    }
    return render(request, 'menu/menu.html', context)

def main_dishes_list(request):
    
    main_dishes_list = MenuItem.objects.filter(catgory_id=4).values()
    context = {
        'main_dishes_list': main_dishes_list
    }
    return render(request, 'menu/menu.html', context)

def desserts_list(request):
    
    desserts_list = MenuItem.objects.filter(catgory_id=5).values()
    context = {
        'desserts_list': desserts_list
    }
    return render(request, 'menu/menu.html', context)


