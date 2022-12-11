from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic as views

from PeopleSite.common.forms import PhotoCommentForm
from PeopleSite.common.models import PhotoLike
from PeopleSite.photos.forms import PhotoCreateForm
from PeopleSite.photos.models import Photo


class PhotoAddView(LoginRequiredMixin, views.CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super(PhotoAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('user details', kwargs={'pk': self.request.user.pk})


class PhotoDetailsView(LoginRequiredMixin, views.DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.person
        context['comment_form'] = PhotoCommentForm()
        context['likes_count'] = self.object.photolike_set.count()
        context['has_user_liked_photo'] = PhotoLike.objects.filter(photo_id=self.object.pk, person_id=self.request.user.pk)

        return context


class PhotoEditView(LoginRequiredMixin, views.UpdateView):
    fields = ('photo', 'description')
    model = Photo
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse('user details', kwargs={'pk': self.request.user.pk})


class PhotoDeleteView(LoginRequiredMixin, views.DeleteView):
    fields = '__all__'
    model = Photo
    template_name = 'photos/photo-delete-page.html'

    def get_success_url(self):
        return reverse('user details', kwargs={'pk': self.request.user.pk})
