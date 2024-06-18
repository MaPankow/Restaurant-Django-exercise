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
        def clean(self):
            cleaned_data = super().clean()
            num_guests = cleaned_data.get('num_guests')
        # Some cleaning logic
            if num_guests < 30:
                self.add_error('num_guests', 'Sorry, we are booked up.')
                return cleaned_data


