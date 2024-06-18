from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ReservationModelForm
from django.urls import reverse
from django.http import HttpResponse
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
# Create your views here.

# class ReservationView(TemplateView):
#     template_name = "reservations/reservations.html"

# def reserve_table(request):
#     if request.method == 'POST':
#         form = ReservationModelForm(request.POST)   
#         print(request.POST)
        # if form.is_valid(): # guckt, ob die Daten im Formular gültig sind
        #     dates = Reservation.objects.all().filter('date')
        #     new_guests = request.num_guests
        #     for date in dates:
        #         guests_per_date = []
        #         if guests_per_date + new_guests <= 30:
        #             form = ReservationModelForm(request.POST)
        #             reservation = form.save()
        #             guests_per_date = guests_per_date + new_guests
        #             return HttpResponse('You have just successfully reserved a table! See you soon!')
        #         else:
        #             return HttpResponse("Booked up")
                
            
          
    # else:
    #     context = {
    #         'form': ReservationModelForm()
    #     }
    #    return render(request, 'reservations/reservations.html', "context")
    
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        #date = form['date'].value() #gibt das Datum der incoming guests raus
        incoming_guests = int(form['num_guests'].value()) #gibt die Nummer der incoming guests raus
        if form.is_valid():
            total_guests = sum(r.num_guests for r in Reservation.objects.filter(date=form.cleaned_data['date']))
            if total_guests + incoming_guests <= 30:
                form.save()
                return redirect('reservation')
            else: 
                return HttpResponse("Sorry, we are booked up for this evening.")
                
    else:
        
        form = ReservationModelForm()
        
        return render(request, 'reservations/reservations.html', {'form':form})


        

        # for date in form:
            
        #     guests_count = guests_count + incoming_guests
            # if guests_count + incoming_guests <= 30:
            #     reservation = form.save()
            #     guests_count = guests_count + incoming_guests
            #     print(guests_count)
            #     return HttpResponse('You have just successfully reserved a table! See you soon!')
            # else:    
            #     return HttpResponse("Booked up")
                
        
    
# Das Mistvieh von Schleife zählt die Gäste immer noch nicht! (Aber trägt sie schon mal in die DB ein, also noch mal mit normaler for-Schleife probieren)


#das ist nur für die Restaurantbetreiber, die Reservierungen sollen auf einer html angezeigt werden
@login_required(login_url='/admin')
def view_reservations(request):
    guests_list = Reservation.objects.all().order_by('date')
    context = {
        'guests_list': guests_list
    }
    return render(request, 'reservations/guests_list.html', context)

#Klasse für die API
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all().order_by('date')
    serializer_class = ReservationSerializer
    
class ReservationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing the menu items.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
