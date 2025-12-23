from django.shortcuts import render

# Create your views here.
def listings(request):
    return render(request, 'listings/listings.html')


def listings(request, listing_id):
    return render(request, 'listings/listings.html')


def search (request):
    return render(request, 'listings/search.html')