from django.shortcuts import render, get_object_or_404
from .models import Listing

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/index.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset = Listing.objects.all()
    # Add filters here if needed (keywords, city, etc.)
    context = {
        'listings': queryset
    }
    return render(request, 'listings/search.html', context)


