window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Force video play
document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('hero-video');
    if (video) {
        video.play().catch(function(error) {
            console.log("Video autoplay failed, waiting for user interaction.");
        });
    }
});

// Mobile menu toggle
document.querySelector('.menu-toggle')?.addEventListener('click', function() {
    document.querySelector('.nav-links').classList.toggle('active');
});
// Room Filtering and Sorting
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const roomContainer = document.getElementById('room-container');
    const priceSort = document.getElementById('price-sort');

    if (!roomContainer) return;

    function getRooms() {
        return Array.from(document.querySelectorAll('.hotel-card'));
    }

    function filterRooms() {
        const activeBtn = document.querySelector('.filter-btn.active');
        if (!activeBtn) return;
        
        const activeFilter = activeBtn.dataset.filter;
        const rooms = getRooms();
        
        rooms.forEach(room => {
            const capacity = room.getAttribute('data-capacity');
            let show = false;

            if (activeFilter === 'all') {
                show = true;
            } else if (activeFilter === '4') {
                show = parseInt(capacity) >= 4;
            } else {
                show = capacity === activeFilter;
            }

            if (show) {
                room.style.display = 'block';
                room.style.opacity = '1';
            } else {
                room.style.display = 'none';
                room.style.opacity = '0';
            }
        });
    }

    function sortRooms() {
        const sortValue = priceSort.value;
        const rooms = getRooms();
        
        if (sortValue === 'default') return;

        rooms.sort((a, b) => {
            const priceA = parseFloat(a.getAttribute('data-price'));
            const priceB = parseFloat(b.getAttribute('data-price'));
            return sortValue === 'low' ? priceA - priceB : priceB - priceA;
        });

        rooms.forEach(room => {
            roomContainer.appendChild(room);
        });
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterRooms();
        });
    });

    if (priceSort) {
        priceSort.addEventListener('change', sortRooms);
    }
    
    // Initial filter call
    filterRooms();
});
