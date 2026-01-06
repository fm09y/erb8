from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # Pages app
    path('', include('pages.urls', namespace='pages')),
    
    # Listings app
    path('listings/', include('listings.urls', namespace='listings')),
    
    # Accounts app
    path('accounts/', include('accounts.urls', namespace='accounts')),
    
    # Contacts app
    path('contacts/', include('contacts.urls', namespace='contacts')),
    
    # Admin site
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()

# Customize Django admin headers
admin.site.site_header = 'Clinic Administration'
admin.site.site_title = 'Clinic Admin Portal'
admin.site.index_title = 'Welcome to Clinic Portal'


