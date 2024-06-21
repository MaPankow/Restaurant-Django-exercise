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

    
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        #date = form['date'].value() #gibt das Datum der incoming guests raus
        incoming_guests = int(form['num_guests'].value()) #gibt die Nummer der incoming guests raus
        if form.is_valid():
            total_guests = sum(r.num_guests for r in Reservation.objects.filter(date=form.cleaned_data['date']))  
            context = {
                'guest': {
                    'date': form['date'].value(),
                    'time': form['time'].value(),
                }
            }
            if total_guests + incoming_guests <= 30:
                form.save()
                return render(request, 'reservations/reservation_success.html', context)
            else: 
                return render(request, 'reservations/reservation_fail.html')
                
    else:
        
        form = ReservationModelForm()
        
        return render(request, 'reservations/reservations.html', {'form':form})

                
        
    


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
