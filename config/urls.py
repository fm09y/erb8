from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # Pages app
    path('', include(('pages.urls', 'pages'), namespace='pages')),

    # Listings app
    path('listings/', include(('listings.urls', 'listings'), namespace='listings')),

    # Admin site
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()

# Customize Django admin headers
admin.site.site_header = 'Clinic Administration'
admin.site.site_title = 'Clinic Admin Portal'
admin.site.index_title = 'Welcome to Clinic Portal'
