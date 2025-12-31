from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "district", "rooms", "service", "doctor", "list_date")
    list_display_links = ("title", "district")
    list_filter = ("district", "doctor", "list_date")
    search_fields = ("title", "district", "doctor__name")
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
