from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic as views

from PeopleSite.common.forms import PhotoCommentForm, MessageCreateForm, SearchForm
from PeopleSite.common.models import PhotoLike, MessagePerson
from PeopleSite.photos.models import Photo

UserModel = get_user_model()

def index(request):
    search_form = SearchForm(request.GET)
    age_pattern_lower = None
    age_pattern_higher = None
    gender_pattern = None
    if search_form.is_valid():
        age_pattern_lower = search_form.cleaned_data['age_lower']
        age_pattern_higher = search_form.cleaned_data['age_higher']
        gender_pattern = search_form.cleaned_data['gender']

    people = UserModel.objects.all()

    if age_pattern_lower or age_pattern_higher or gender_pattern:
        if not age_pattern_lower:
            age_pattern_lower = 0
        if not age_pattern_higher:
            age_pattern_higher = 150
        if not gender_pattern:
            people = UserModel.objects.filter(
                Q(age__gte=age_pattern_lower) & Q(age__lte=age_pattern_higher))
        else:
            people = UserModel.objects.filter(
            Q(age__gte=age_pattern_lower) & Q(age__lte=age_pattern_higher) & Q(gender=gender_pattern)
            )

    context = {
        'people': people,
        'search_form': search_form,
    }

    return render(request,'index.html',context,)


@login_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects.filter(photo_id=photo_id, user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect('photo details', pk=photo_id)


@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    person = UserModel.objects.filter(pk=request.user.pk).get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.person = person
        comment.save()

    return redirect('photo details', pk=photo_id)
