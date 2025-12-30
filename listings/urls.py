from django.urls import path
from . import views

# Namespace for this app so {% url 'listings:...' %} works
app_name = 'listings'

urlpatterns = [
    # Main listings page (list of all listings)
    path('', views.index, name='index'),

    # Individual listing detail page
    path('<int:listing_id>/', views.listing, name='detail'),

    # Search page
    path('search/', views.search, name='search'),
]
