from django import forms

from .models import Reservation

class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'name',
            'date',
            'time',
            'num_guests',
        ]