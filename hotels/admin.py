from django.contrib import admin
from django.utils.html import format_html
from .models import Hotel, RoomType, Amenity, GalleryImage, Booking, Review, RoomImage

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_display')
    
    def icon_display(self, obj):
        return format_html('<i class="fa {}"></i> {}', obj.icon, obj.icon)
    icon_display.short_description = 'Icon'

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 3

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 2

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'star_rating', 'phone', 'email', 'main_image_preview')
    list_filter = ('star_rating', 'amenities')
    search_fields = ('name', 'address')
    inlines = [GalleryImageInline, RoomTypeInline]
    
    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="50" style="border-radius: 5px;" />', obj.main_image.url)
        return "No Image"
    main_image_preview.short_description = 'Preview'

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'price_per_night', 'capacity')
    list_filter = ('hotel', 'capacity')
    inlines = [RoomImageInline]
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'room_type', 'hotel', 'check_in', 'check_out', 'guests', 'status', 'status_colored', 'created_at')
    list_filter = ('status', 'hotel', 'check_in')
    search_fields = ('full_name', 'email', 'phone')
    list_editable = ('status',)
    date_hierarchy = 'check_in'

    def status_colored(self, obj):
        colors = {
            'pending': '#ffc107', # Yellow
            'confirmed': '#28a745', # Green
            'cancelled': '#dc3545', # Red
        }
        return format_html(
            '<span style="color: white; background: {}; padding: 3px 10px; border-radius: 10px; font-size: 0.8rem;">{}</span>',
            colors.get(obj.status, '#6c757d'),
            obj.get_status_display()
        )
    status_colored.short_description = 'Durum'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'hotel', 'rating_stars', 'created_at')
    list_filter = ('rating', 'hotel')
    search_fields = ('user_name', 'comment')

    def rating_stars(self, obj):
        return format_html(''.join(['<i class="fas fa-star" style="color: #ffc107;"></i>' for _ in range(obj.rating)]))
    rating_stars.short_description = 'Puan'

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'caption', 'image_preview')
    list_filter = ('hotel',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 10px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Önizleme'
