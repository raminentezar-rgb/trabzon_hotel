from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Hotel, RoomType, Booking

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})

def book_room(request):
    if request.method == 'POST':
        hotel = Hotel.objects.first() # For single hotel demo
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests', 2)
        room_id = request.POST.get('room_id')
        
        if full_name and email and check_in and check_out:
            room = None
            if room_id:
                room = RoomType.objects.filter(pk=room_id).first()
            
            # Double booking check
            if room:
                overlap = Booking.objects.filter(
                    room_type=room,
                    status__in=['pending', 'confirmed'],
                    check_in__lt=check_out,
                    check_out__gt=check_in
                ).exists()
                
                if overlap:
                    messages.error(request, 'Seçtiğiniz tarihler arasında bu oda zaten rezerve edilmiş. Lütfen başka bir tarih seçin.')
                    return redirect(request.META.get('HTTP_REFERER', 'core:home'))
                
            Booking.objects.create(
                hotel=hotel,
                room_type=room,
                full_name=full_name,
                email=email,
                phone=phone,
                check_in=check_in,
                check_out=check_out,
                guests=guests
            )
            messages.success(request, 'Rezervasyon talebiniz başarıyla alındı. Sizinle en kısa sürede iletişime geçeceğiz.')
        else:
            messages.error(request, 'Lütfen tüm zorunlu alanları doldurun.')
            
    return redirect('core:home')

def gallery_list(request):
    hotel = Hotel.objects.first() # For single hotel demo
    gallery = hotel.gallery.all()
    return render(request, 'hotels/gallery.html', {'hotel': hotel, 'gallery': gallery})

def room_detail(request, pk):
    room = get_object_or_404(RoomType, pk=pk)
    booked_dates = Booking.objects.filter(
        room_type=room, 
        status__in=['pending', 'confirmed']
    ).values('check_in', 'check_out')
    
    # Format dates for JS
    disabled_dates = []
    for booking in booked_dates:
        disabled_dates.append({
            'from': booking['check_in'].strftime('%Y-%m-%d'),
            'to': booking['check_out'].strftime('%Y-%m-%d')
        })
        
    return render(request, 'hotels/room_detail.html', {
        'room': room, 
        'hotel': room.hotel,
        'disabled_dates': disabled_dates
    })

def room_list(request):
    hotel = Hotel.objects.first()
    rooms = hotel.room_types.all()
    return render(request, 'hotels/room_list.html', {'hotel': hotel, 'rooms': rooms})
