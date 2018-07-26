from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime as dt
from .models import Image, Comment, Profile
from .forms import NewImageForm, NewProfileForm


# Create your views here.


def welcome(request):
    title = 'Welcome'
    return render(request, 'welcome.html', {'title': title})

def all_images(request):
    date = dt.date.today()
    images = Image.get_all()
    comments = Comment.get_comments()
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def my_profile(request,profile_id):
    date = dt.date.today()
    profile = Profile.objects.filter(user_id=profile_id).first()
    images = Image.objects.filter(user_id=request.user.id)
    return render(request, 'profile.html', locals())

def explore(request):
    date = dt.date.today()
    profiles = Profile.get_profiles()
    return render(request, 'explore.html', {"date": date, "profiles": profiles})


def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})


