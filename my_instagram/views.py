from django.shortcuts import render
import datetime as dt
from my_instagram.models import Image, Comment


# Create your views here.


def welcome(request):
    title = 'Welcome'
    return render(request, 'welcome.html', {'title': title})

def all_images(request):
    date = dt.date.today()
    images = Image.get_all()
    comments = Comment.get_comments()
    return render(request, 'index.html', {"date": date, "images": images, "comments": comments})
