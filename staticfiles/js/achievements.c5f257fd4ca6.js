document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    const pastBtn = document.getElementById('pastBtn');
    const presentBtn = document.getElementById('presentBtn');
    const pastAchievements = document.getElementById('pastAchievements');
    const presentAchievements = document.getElementById('presentAchievements');
    const scrollTopBtn = document.getElementById('scrollTopBtn');

    // Toggle between past and present achievements
    function showPastAchievements() {
        pastAchievements.classList.remove('hidden');
        presentAchievements.classList.add('hidden');
        pastBtn.classList.remove('text-primary', 'bg-white', 'border-primary');
        pastBtn.classList.add('text-white', 'bg-primary');
        presentBtn.classList.add('text-primary', 'bg-white', 'border-primary');
        presentBtn.classList.remove('text-white', 'bg-primary');
    }

    function showPresentAchievements() {
        presentAchievements.classList.remove('hidden');
        pastAchievements.classList.add('hidden');
        presentBtn.classList.remove('text-primary', 'bg-white', 'border-primary');
        presentBtn.classList.add('text-white', 'bg-primary');
        pastBtn.classList.add('text-primary', 'bg-white', 'border-primary');
        pastBtn.classList.remove('text-white', 'bg-primary');
    }

    // Create achievement card
    function createAchievementCard(achievement) {
        return `
            <div class="achievement-card bg-white rounded-xl shadow-lg overflow-hidden">
                <div class="relative h-48 overflow-hidden">
                    <img src="${achievement.image}" alt="${achievement.title}" class="w-full h-full object-cover">
                    <div class="absolute top-4 right-4 bg-primary text-white px-3 py-1 rounded-full text-sm font-semibold">
                        ${achievement.year}
                    </div>
                </div>
                <div class="p-6">
                    <div class="flex items-center mb-4">
                        <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center text-primary">
                            <i class="${achievement.icon} text-xl"></i>
                        </div>
                        <h3 class="text-xl font-bold ml-3 text-gray-800">${achievement.title}</h3>
                    </div>
                    <p class="text-gray-600 leading-relaxed">
                        ${achievement.description}
                    </p>
                </div>
            </div>
        `;
    }

    // Render achievements
    function renderAchievements() {
        // Render past achievements
        pastAchievements.innerHTML = achievementsData.past
            .map(achievement => createAchievementCard(achievement))
            .join('');

        // Render present achievements
        presentAchievements.innerHTML = achievementsData.present
            .map(achievement => createAchievementCard(achievement))
            .join('');
    }

    // Scroll to top functionality
    function toggleScrollButton() {
        if (window.scrollY > 200) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    }

    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    // Event listeners
    pastBtn.addEventListener('click', showPastAchievements);
    presentBtn.addEventListener('click', showPresentAchievements);
    scrollTopBtn.addEventListener('click', scrollToTop);
    window.addEventListener('scroll', toggleScrollButton);

    // Initialize
    renderAchievements();
    showPastAchievements(); // Show past achievements by default
    toggleScrollButton(); // Check initial scroll position
});
