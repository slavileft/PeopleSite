from django import views
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect

from PeopleSite.chat.forms import MessageForm
from PeopleSite.chat.models import ThreadModel, MessageModel

UserModel = get_user_model()

class CreateThread(views.View):
    def post(self, request, pk,  *args, **kwargs):
        receiver= UserModel.objects.filter(pk=pk).get()

        if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
            thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
            return redirect('thread', pk=thread.pk)
        elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
            thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
            return redirect('thread', pk=thread.pk)

        sender_thread = ThreadModel(
            user=request.user,
            receiver=receiver
        )
        sender_thread.save()
        return redirect('thread', pk=sender_thread.pk)


class ListThreads(views.View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        context = {
        'threads': threads
        }
        return render(request, 'chat/inbox.html', context)


class CreateMessage(views.View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
          receiver = thread.user
        else:
          receiver = thread.receiver
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message'),
          )
        message.save()
        return redirect('thread', pk=pk)


class ThreadView(views.View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
          'thread': thread,
          'form': form,
          'message_list': message_list
        }
        return render(request, 'chat/thread.html', context)