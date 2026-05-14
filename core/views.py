from django.shortcuts import render
from django.conf import settings

from hotels.models import Hotel

from hotels.models import Hotel

def home(request):
    hotel = Hotel.objects.first()
    if not hotel:
        # Fallback if no hotel exists yet
        return render(request, 'home.html', {'hero_image': '/static/img/hero.png'})
    
    context = {
        'hotel': hotel,
        'rooms': hotel.room_types.all()[:6],
        'gallery': hotel.gallery.all()[:3],
        'reviews': hotel.reviews.all().order_by('-created_at'),
        'hero_image': hotel.main_image.url if hotel.main_image else '/static/img/hero.png',
    }
    return render(request, 'home.html', context)
