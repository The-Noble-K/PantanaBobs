from django.shortcuts import render
from photos.models import Photo

def photo_index(request):
    photos = Photo.objects.all()
    context = { "photos": photos }
    return render(request, "photo_index.html", context)

