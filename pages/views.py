from django.shortcuts import render
#from django.core.paginator import Paginator
from .models import Listing

'''def index(request):
    return render(request, 'pages/index.html', {'anything': 'something', 'number: 1234'}
def about(request):
    print(request, request.path)
    return render(request, 'pages/about.html')'''

def index(request):
    listings=Listing.objects.all()
    context = {'Listings': Listings}
    return render(request, 'pages/index.html', context)

def index(request):
    print(request, request.path)
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')



def listings(request):
    """Display all listings with pagination"""
    listings_list = Listing.objects.all().order_by('-id')
    
    # Pagination (3 per page)
    paginator = Paginator(listings_list, 3)
    page_number = request.GET.get('page')
    listings = paginator.get_page(page_number)
    
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    """Single listing detail page"""
    listing = Listing.objects.get(id=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

# Keep your existing views (but rename index to listings)
