from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

# Create your views here.
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

def booking_list(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

