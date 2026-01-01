from django.shortcuts import render
from listings.models import Listing
from doctors.models import Doctor
from listings.choices import district_choices, room_choices, rooms_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'district_choices': district_choices,
        'room_choices': room_choices,
        "rooms_choices": rooms_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    doctors = Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors = Doctor.objects.filter(is_mvp=True)
    total_mvp = mvp_doctors.count()
    context = {
        "doctors": doctors, 
        "mvp_doctors": mvp_doctors, 
        "total_mvp": total_mvp
    }
    return render(request, 'pages/about.html', context)
