// Simple client-side theme toggle
(function() {
    console.log("Theme toggle script loaded");
    
    const wrapper = document.querySelector(".theme-wrapper");
    const toggleBtn = document.getElementById("toggle-theme");

    if (!wrapper) {
        console.error("Theme wrapper not found");
        return;
    }
    
    if (!toggleBtn) {
        console.error("Toggle button not found");
        return;
    }

    // Initialize theme from localStorage
    const savedTheme = localStorage.getItem("theme") || "light";
    if (savedTheme === "dark") {
        wrapper.classList.add("dark-theme");
    }

    // Click handler for toggle button
    toggleBtn.addEventListener("click", function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        console.log("Toggle clicked - current:", wrapper.classList.contains("dark-theme") ? "dark" : "light");
        
        // Toggle the dark-theme class
        wrapper.classList.toggle("dark-theme");
        
        // Save preference
        const isDark = wrapper.classList.contains("dark-theme");
        localStorage.setItem("theme", isDark ? "dark" : "light");
        
        console.log("Theme switched to:", isDark ? "dark" : "light");
        
        // Try to sync with server (optional, won't break if it fails)
        const csrfToken = getCsrfToken();
        if (csrfToken) {
            fetch("/accounts/set-theme/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({ theme: isDark ? "dark" : "light" })
            })
            .then(res => res.json())
            .then(data => console.log("Server sync:", data))
            .catch(err => console.warn("Server sync error (non-critical):", err));
        }
    });

    // Extract CSRF token from page
    function getCsrfToken() {
        // Try to find in meta tag
        const meta = document.querySelector('meta[name="csrf-token"]');
        if (meta) return meta.getAttribute('content');
        
        // Try to find in hidden input
        const input = document.querySelector('input[name="csrfmiddlewaretoken"]');
        if (input) return input.value;
        
        // Try to extract from cookies
        const name = 'csrftoken';
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    console.log("Theme toggle ready");
})();
