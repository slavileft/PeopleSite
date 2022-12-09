from django.contrib import admin

from PeopleSite.chat.models import ThreadModel, MessageModel


@admin.register(ThreadModel)
class ThreadModelAdmin(admin.ModelAdmin):
    pass


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    pass
