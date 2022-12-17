from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class ThreadModel(models.Model):
    user = models.ForeignKey(UserModel,
                             on_delete=models.CASCADE,
                             related_name='+',
                             )
    receiver = models.ForeignKey(UserModel,
                                 on_delete=models.CASCADE,
                                 related_name='+',
                                 )
    has_unread = models.BooleanField(default=False)

class MessageModel(models.Model):
    MAX_BODY_LENGTH = 1000
    thread = models.ForeignKey('ThreadModel',
                               related_name='+',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               )
    sender_user = models.ForeignKey(UserModel,
                                    on_delete=models.CASCADE,
                                    related_name='+',
                                    )
    receiver_user = models.ForeignKey(UserModel,
                                      on_delete=models.CASCADE,
                                      related_name='+',
                                      )
    body = models.CharField(max_length=MAX_BODY_LENGTH)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.body

