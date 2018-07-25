from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from my_instagram import views

urlpatterns=[
    url(r'^$', views.all_images, name='welcome'),
    url(r'^what_profile/(?P<profile_id>\d+)', views.my_profile, name='profile'),
    url(r'^explore_more/', views.explore, name='my_explore'),
    url(r'^new/image$', views.new_image, name='new-image'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)