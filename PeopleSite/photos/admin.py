from django.contrib import admin

from PeopleSite.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'publication_date', 'person')
