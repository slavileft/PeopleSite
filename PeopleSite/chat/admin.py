from django.contrib import admin

from PeopleSite.chat.models import ThreadModel, MessageModel


@admin.register(ThreadModel)
class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'receiver')


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'sender_user', 'receiver_user', 'body', 'date', 'is_read')
