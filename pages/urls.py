
# from django.urls import path
# from . import views

# app_name = 'pages'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),  # ← Added slash!
# ]

from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    # path('listings/', views.listings, name='listings'),
    # path('listing/<int:listing_id>/', views.listing, name='listing'),
    path('about/', views.about, name='about'),
]