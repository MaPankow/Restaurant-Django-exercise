from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Reservation
from django.contrib.auth.decorators import login_required
from .forms import ReservationModelForm

# Create your views here.

# class ReservationView(TemplateView):
#     template_name = "reservations/reservations.html"
def reserve_table(request):
    return render(request, 'reservations/reservations.html')


#das ist nur für die Restaurantbetreiber, die Reservierungen sollen auf einer html angezeigt werden
@login_required
def view_reservations(request):
    return render(request, 'reservations/guests_list.html')
    # guests_list = Reservation.objects.all().order_by('date', 'time')
    # context = {
    #     'guests_list': guests_list
    # }
    # return render(request, 'reservations/guests_list.html', context)

