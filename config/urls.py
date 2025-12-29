

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns = [
    #path('', include ('pages.uadmin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('listings/', include ('listings.urls', namespace='listings')),
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings. MEDIA_ROOT) + debug_toolbar_urls()

admin.site.site_header = 'Clinic Administration'
admin.site.site_title = 'Clinic Admin Portal'
admin.site.index_title = 'Welcome to Clinic Portal'

