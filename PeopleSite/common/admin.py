from django.contrib import admin

from PeopleSite.common.models import PhotoComment, MessagePerson


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'publication_date_and_time', 'photo')


@admin.register(MessagePerson)
class MessagePersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'publication_date_and_time', 'person')
