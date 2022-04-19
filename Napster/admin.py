from django.contrib import admin
from .models import Song, Album

# Register your models here.
admin.site.register(Song)
admin.site.register(Album)
admin.site.site_header = "Napster Admin"
admin.site.site_title = "Napster Admin Portal"  # Title for the admin page
admin.site.index_title = "Welcome to Napster Admin Portal"  # Title for the index page

