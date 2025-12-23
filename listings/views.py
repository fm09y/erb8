

# Create your views here.

from django.shortcuts import render

def listings(request):
    return render(request, 'listings/index.html')

def listing(request, listing_id):
    return render(request, 'listings/listing.html', {'listing_id': listing_id})

def search(request):
    return render(request, 'listings/search.html')

