document.addEventListener('DOMContentLoaded', () => {
    const alumniGrid = document.getElementById('alumniGrid');
    const template = document.getElementById('alumniCardTemplate');
    const searchInput = document.getElementById('searchInput');
    const maps = new Map(); // Store map instances

    // Custom map styles
    const mapStyles = [
        {
            name: 'Modern Blue',
            styles: [{"featureType":"water","elementType":"geometry","stylers":[{"color":"#e9e9e9"},{"lightness":17}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffffff"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#ffffff"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#ffffff"},{"lightness":16}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#f5f5f5"},{"lightness":21}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#dedede"},{"lightness":21}]},{"elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#ffffff"},{"lightness":16}]},{"elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#333333"},{"lightness":40}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#f2f2f2"},{"lightness":19}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#fefefe"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#fefefe"},{"lightness":17},{"weight":1.2}]}]
        },
        {
            name: 'Night Mode',
            styles: [{"elementType":"geometry","stylers":[{"color":"#242f3e"}]},{"elementType":"labels.text.fill","stylers":[{"color":"#746855"}]},{"elementType":"labels.text.stroke","stylers":[{"color":"#242f3e"}]},{"featureType":"administrative.locality","elementType":"labels.text.fill","stylers":[{"color":"#d59563"}]},{"featureType":"poi","elementType":"labels.text.fill","stylers":[{"color":"#d59563"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#263c3f"}]},{"featureType":"poi.park","elementType":"labels.text.fill","stylers":[{"color":"#6b9a76"}]},{"featureType":"road","elementType":"geometry","stylers":[{"color":"#38414e"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"color":"#212a37"}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#9ca5b3"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#746855"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#1f2835"}]},{"featureType":"road.highway","elementType":"labels.text.fill","stylers":[{"color":"#f3d19c"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#2f3948"}]},{"featureType":"transit.station","elementType":"labels.text.fill","stylers":[{"color":"#d59563"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#17263c"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#515c6d"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#17263c"}]}]
        },
        {
            name: 'Retro',
            styles: [{"elementType":"geometry","stylers":[{"color":"#ebe3cd"}]},{"elementType":"labels.text.fill","stylers":[{"color":"#523735"}]},{"elementType":"labels.text.stroke","stylers":[{"color":"#f5f1e6"}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#c9b2a6"}]},{"featureType":"administrative.land_parcel","elementType":"geometry.stroke","stylers":[{"color":"#dcd2be"}]},{"featureType":"administrative.land_parcel","elementType":"labels.text.fill","stylers":[{"color":"#ae9e90"}]},{"featureType":"landscape.natural","elementType":"geometry","stylers":[{"color":"#dfd2ae"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#dfd2ae"}]},{"featureType":"poi","elementType":"labels.text.fill","stylers":[{"color":"#93817c"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#a5b076"}]},{"featureType":"poi.park","elementType":"labels.text.fill","stylers":[{"color":"#447530"}]},{"featureType":"road","elementType":"geometry","stylers":[{"color":"#f5f1e6"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#fdfcf8"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#f8c967"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#e9bc62"}]},{"featureType":"road.highway.controlled_access","elementType":"geometry","stylers":[{"color":"#e98d58"}]},{"featureType":"road.highway.controlled_access","elementType":"geometry.stroke","stylers":[{"color":"#db8555"}]},{"featureType":"road.local","elementType":"labels.text.fill","stylers":[{"color":"#806b63"}]},{"featureType":"transit.line","elementType":"geometry","stylers":[{"color":"#dfd2ae"}]},{"featureType":"transit.line","elementType":"labels.text.fill","stylers":[{"color":"#8f7d77"}]},{"featureType":"transit.line","elementType":"labels.text.stroke","stylers":[{"color":"#ebe3cd"}]},{"featureType":"transit.station","elementType":"geometry","stylers":[{"color":"#dfd2ae"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"color":"#b9d3c2"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#92998d"}]}]
        }
    ];

    // Create achievement card HTML
    function createAchievementHTML(achievement) {
        return `
            <div class="achievement-item bg-accent/5 rounded p-2">
                <div class="flex justify-between items-start">
                    <h4 class="text-gray-800 text-sm font-medium">${achievement.title}</h4>
                    <span class="text-xs text-primary font-medium">${achievement.year}</span>
                </div>
                <p class="text-gray-600 text-xs mt-0.5">${achievement.description}</p>
            </div>
        `;
    }

    // Render all alumni cards
    function renderAlumniCards(alumniList = alumniData) {
        alumniGrid.innerHTML = '';
        alumniList.forEach(alumni => {
            const card = template.content.cloneNode(true);
            
            // Set basic information
            card.querySelector('img').src = alumni.image;
            card.querySelector('h2').textContent = alumni.name;
            card.querySelector('p.text-primary').textContent = alumni.domain;
            card.querySelector('.degree').textContent = alumni.degree;
            card.querySelector('.company').textContent = alumni.company;
            card.querySelector('.domain').textContent = alumni.domain;

            // Set skills
            const skillsContainer = card.querySelector('.skills');
            alumni.skills.forEach(skill => {
                const skillBadge = document.createElement('span');
                skillBadge.className = 'px-3 py-1 bg-accent/10 text-primary rounded-full text-sm font-medium';
                skillBadge.textContent = skill;
                skillsContainer.appendChild(skillBadge);
            });

            // Set achievements
            const achievementsContainer = card.querySelector('.achievements');
            if (alumni.achievements && alumni.achievements.length > 0) {
                alumni.achievements.forEach(achievement => {
                    achievementsContainer.innerHTML += createAchievementHTML(achievement);
                });
            } else {
                achievementsContainer.innerHTML = `
                    <p class="text-gray-500 text-sm italic">No achievements listed yet.</p>
                `;
            }

            // Set social media links
            card.querySelector('.linkedin').href = alumni.socialMedia.linkedin;
            card.querySelector('.twitter').href = alumni.socialMedia.twitter;
            card.querySelector('.email').href = `mailto:${alumni.email}`;
            card.querySelector('.phone').href = `tel:${alumni.mobile}`;

            // Add the card to the grid
            const cardElement = alumniGrid.appendChild(card);

            // Initialize Google Map with random style
            setTimeout(() => {
                const mapContainer = cardElement.querySelector('.map-container');
                const randomStyle = mapStyles[Math.floor(Math.random() * mapStyles.length)];
                
                // Add some random offset to the location to make maps more diverse
                const offset = 0.01; // Approximately 1km
                const randomLat = alumni.location.lat + (Math.random() - 0.5) * offset;
                const randomLng = alumni.location.lng + (Math.random() - 0.5) * offset;

                const map = new google.maps.Map(mapContainer, {
                    center: { lat: randomLat, lng: randomLng },
                    zoom: 13,
                    styles: randomStyle.styles,
                    disableDefaultUI: true, // Disable default UI controls
                    zoomControl: true // But keep zoom control
                });

                // Add custom marker
                const marker = new google.maps.Marker({
                    position: { lat: randomLat, lng: randomLng },
                    map: map,
                    title: alumni.name,
                    animation: google.maps.Animation.DROP
                });

                // Add info window
                const infoWindow = new google.maps.InfoWindow({
                    content: `
                        <div class="p-2">
                            <h3 class="font-bold">${alumni.name}</h3>
                            <p>${alumni.location.address}</p>
                        </div>
                    `
                });

                marker.addListener('click', () => {
                    infoWindow.open(map, marker);
                });

                maps.set(alumni.id, map);
            }, 100);
        });
    }

    // Search functionality
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        const filteredAlumni = alumniData.filter(alumni => {
            return (
                alumni.name.toLowerCase().includes(searchTerm) ||
                alumni.company.toLowerCase().includes(searchTerm) ||
                alumni.domain.toLowerCase().includes(searchTerm) ||
                alumni.skills.some(skill => skill.toLowerCase().includes(searchTerm)) ||
                alumni.achievements.some(achievement => 
                    achievement.title.toLowerCase().includes(searchTerm) ||
                    achievement.description.toLowerCase().includes(searchTerm)
                )
            );
        });
        renderAlumniCards(filteredAlumni);
    });

    // Initial render
    renderAlumniCards();
});
