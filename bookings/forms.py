from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name',
            'department',
            'contact',
            'email',
            'title',
            'purpose',
            'date',
            'start_time',
            'end_time',
            'expected_attendees',
            'audio_visual',
            'break_tea',
            'lunch'
            ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }