from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ReservationModelForm
from django.urls import reverse
from django.http import HttpResponse
from .models import Reservation
# Create your views here.

# class ReservationView(TemplateView):
#     template_name = "reservations/reservations.html"
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        reservation = form.save()
        return HttpResponse('You have just successfully reserved a table! See you soon!')

    else:
        context = {
            'form': ReservationModelForm()
        }
        return render(request, 'reservations/reservations.html')
    



#das ist nur für die Restaurantbetreiber, die Reservierungen sollen auf einer html angezeigt werden
@login_required(login_url='/admin')
def view_reservations(request):
    guests_list = Reservation.objects.all().order_by('date')
    context = {
        'guests_list': guests_list
    }
    return render(request, 'reservations/guests_list.html', context)
    

