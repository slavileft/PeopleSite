from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic as views

from PeopleSite.accounts.forms import UserRegisterForm
from PeopleSite.chat.forms import ThreadForm

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    template_name = 'accounts/user-register-page.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'accounts/user-login-page.html'
    success_url = reverse_lazy('index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel
    photos_paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = self.object.photo_set.all()
        paginator = Paginator(photos, self.photos_paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['is_owner'] = self.request.user == self.object
        context['thread_form'] = ThreadForm(self.request.POST)
        context['page_obj'] = page_obj

        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = UserModel
    template_name = 'accounts/user-edit-page.html'
    fields = (
        'email',
        'first_name',
        'last_name',
        'age',
        'height',
        'weight',
        'eyes_color',
        'hair_color',
        'profile_picture',
        'gender',
    )

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.request.user.pk})


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
