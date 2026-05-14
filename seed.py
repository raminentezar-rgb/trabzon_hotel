import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from hotels.models import Hotel, RoomType, Amenity, GalleryImage

def seed():
    # Clear existing data
    Hotel.objects.all().delete()
    Amenity.objects.all().delete()
    
    # Create Amenities
    amenities_data = [
        ('Ücretsiz Yüksek Hızlı Wi-Fi', 'fa-wifi'),
        ('Sonsuzluk Havuzu', 'fa-person-swimming'),
        ('A la Carte Restoran', 'fa-utensils'),
        ('Ücretsiz Vale Park Hizmeti', 'fa-square-p'),
        ('Lüks Spa ve Türk Hamamı', 'fa-spa'),
        ('Modern Fitness Merkezi', 'fa-gym'),
        ('Merkezi Klima Sistemi', 'fa-wind'),
        ('Smart TV ve Uydu Yayını', 'fa-tv'),
        ('Havaalanı Transferi', 'fa-plane-departure'),
        ('7/24 Oda Servisi', 'fa-bell'),
        ('Çocuk Kulübü', 'fa-child-reaching'),
        ('Toplantı ve Konferans Salonu', 'fa-handshake'),
    ]
    
    amenities = []
    for name, icon in amenities_data:
        amenity, created = Amenity.objects.get_or_create(name=name, icon=icon)
        amenities.append(amenity)
    
    # The Primary Hotel for the Demo
    hotel = Hotel.objects.create(
        name='Trabzon Royal Palace & Spa',
        description='Trabzon Royal Palace & Spa, Karadeniz\'in masmavi sularıyla yemyeşil dağlarının buluştuğu noktada, misafirlerine krallara layık bir konaklama deneyimi sunuyor. Modern mimarisi, ödüllü şeflerin elinden çıkan lezzetleri ve huzur veren spa merkeziyle şehrin en prestijli adresi.',
        address='Trabzon, Sahil Mevkii, No: 61, Merkez',
        star_rating=5,
        phone='+90 462 777 8899',
        email='info@trabzonroyal.com',
        whatsapp='905001112233',
        instagram='trabzonroyalpalace'
    )
    
    hotel.amenities.add(*amenities)
    
    # Room Types
    rooms = [
        {
            'name': 'Kral Dairesi (Presidential Suite)',
            'description': 'Panoramik deniz manzaralı, jakuzili, geniş oturma alanlı ve özel teraslı en üst düzey konaklama birimimiz.',
            'price_per_night': 12500,
            'capacity': 2
        },
        {
            'name': 'Aile Süiti (Family Connection Room)',
            'description': 'Kalabalık aileler için tasarlanmış, ara kapılı, geniş ve konforlu iki yatak odasından oluşan özel birim.',
            'price_per_night': 7800,
            'capacity': 4
        },
        {
            'name': 'Deluxe Deniz Manzaralı Oda',
            'description': 'Modern dekorasyonu ve eşsiz Karadeniz manzarasıyla huzurlu bir konaklama arayanlar için ideal seçim.',
            'price_per_night': 4200,
            'capacity': 2
        },
        {
            'name': 'Superior Dağ Manzaralı Oda',
            'description': 'Trabzon\'un yemyeşil doğasına bakan, sessiz ve sakin bir atmosferde dinlenmek isteyenler için.',
            'price_per_night': 3500,
            'capacity': 2
        }
    ]
    
    for r_data in rooms:
        RoomType.objects.create(hotel=hotel, **r_data)

    # Sample Reviews
    reviews_data = [
        ('Ahmet Yılmaz', 5, 'Muhteşem bir otel! Karadeniz manzarası eşliğinde kahvaltı yapmak paha biçilemezdi. Personel çok ilgiliydi.'),
        ('Elif Demir', 4, 'Odalar çok temiz ve geniş. Spa merkezi harika, kesinlikle tavsiye ederim. Sadece otopark biraz kalabalıktı.'),
        ('Mustafa Aydın', 5, 'İş seyahati için gelmiştim ama kendimi tatilde gibi hissettim. İnternet hızı mükemmel, konfor üst düzey.'),
        ('Zeynep Kaya', 5, 'Ailemle birlikte kaldık. Çocuklar havuzu çok sevdi. Yemekler çok lezzetliydi, her şey için teşekkürler.')
    ]
    
    from hotels.models import Review
    for user, rating, comment in reviews_data:
        Review.objects.create(hotel=hotel, user_name=user, rating=rating, comment=comment)

    print("Single Hotel Demo with Reviews Seeded Successfully!")

if __name__ == '__main__':
    seed()
