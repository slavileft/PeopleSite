from django.contrib import admin

from PeopleSite.common.models import PhotoComment


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'publication_date_and_time', 'photo')
