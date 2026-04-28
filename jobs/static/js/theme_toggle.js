// Select the wrapper
const wrapper = document.querySelector('.theme-wrapper');

// Load saved theme from localStorage
let darkMode = localStorage.getItem('darkMode');
if (darkMode === 'enabled') {
    wrapper.classList.add('dark-theme');
}

// Toggle function
function toggleTheme() {
    wrapper.classList.toggle('dark-theme');

    // Save preference
    if (wrapper.classList.contains('dark-theme')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
}

// Attach toggle to button
const toggleBtn = document.getElementById('toggle-theme');
if (toggleBtn) {
    toggleBtn.addEventListener('click', toggleTheme);
}
