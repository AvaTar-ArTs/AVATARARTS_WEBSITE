/**
 * AvatarArts Website JavaScript
 * Client-side functionality for avatararts.org
 */

// Initialize the website when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize navigation
    initNavigation();
    
    // Initialize smooth scrolling
    initSmoothScrolling();
    
    // Initialize any interactive elements
    initInteractiveElements();
    
    // Load any dynamic content
    loadDynamicContent();
});

// Initialize navigation functionality
function initNavigation() {
    // Add active class to current page
    const currentPage = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
    
    // Add scroll effect to navbar
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(0, 0, 0, 0.98)';
        } else {
            navbar.style.background = 'rgba(0, 0, 0, 0.95)';
        }
    });
}

// Initialize smooth scrolling for anchor links
function initSmoothScrolling() {
    // Add smooth scrolling to all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Account for fixed navbar
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Initialize interactive elements
function initInteractiveElements() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.feature-card, .stat-card, .theme-card, .collection-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Initialize any modals or popups
    initModals();
    
    // Initialize form validation
    initFormValidation();
}

// Initialize modals
function initModals() {
    // If there are any modals on the page, initialize them
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        // Add event listeners for modal functionality
        const closeBtn = modal.querySelector('.close');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                modal.style.display = 'none';
            });
        }
        
        // Close modal when clicking outside of it
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });
}

// Initialize form validation
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Basic form validation
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });
}

// Load dynamic content
function loadDynamicContent() {
    // Load any dynamic content via AJAX
    loadStats();
    loadInsights();
}

// Load statistics dynamically
function loadStats() {
    // In a real implementation, this would fetch data from an API
    // For now, we'll just log that the function exists
    console.log('Loading statistics...');
    
    // Example of how to fetch data from the API
    /*
    fetch('/api/collection-stats')
        .then(response => response.json())
        .then(data => {
            // Update stat cards with real data
            updateStatCards(data);
        })
        .catch(error => {
            console.error('Error loading stats:', error);
        });
    */
}

// Load insights dynamically
function loadInsights() {
    // In a real implementation, this would fetch data from an API
    console.log('Loading insights...');
    
    // Example of how to fetch data from the API
    /*
    fetch('/api/insights')
        .then(response => response.json())
        .then(data => {
            // Update charts and insights with real data
            updateCharts(data);
        })
        .catch(error => {
            console.error('Error loading insights:', error);
        });
    */
}

// Update stat cards with data
function updateStatCards(data) {
    // Update the stat cards with actual data
    if (data.total_tracks !== undefined) {
        const trackStat = document.querySelector('.stat-card:nth-child(1) h3');
        if (trackStat) trackStat.textContent = data.total_tracks;
    }
    
    if (data.total_albums !== undefined) {
        const albumStat = document.querySelector('.stat-card:nth-child(2) h3');
        if (albumStat) albumStat.textContent = data.total_albums;
    }
    
    if (data.total_repositories !== undefined) {
        const repoStat = document.querySelector('.stat-card:nth-child(3) h3');
        if (repoStat) repoStat.textContent = data.total_repositories;
    }
    
    if (data.avatararts_repositories !== undefined) {
        const avatarartsStat = document.querySelector('.stat-card:nth-child(4) h3');
        if (avatarartsStat) avatarartsStat.textContent = data.avatararts_repositories;
    }
}

// Update charts with data
function updateCharts(data) {
    // This would update the Chart.js charts with real data
    console.log('Updating charts with data:', data);
}

// Utility function to show loading state
function showLoading(element) {
    const originalContent = element.innerHTML;
    element.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>';
    return originalContent;
}

// Utility function to hide loading state
function hideLoading(element, originalContent) {
    element.innerHTML = originalContent;
}

// Utility function to show notification
function showNotification(message, type = 'info') {
    // Create a notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show`;
    notification.setAttribute('role', 'alert');
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // Add to the beginning of the body
    document.body.insertBefore(notification, document.body.firstChild);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Export functions for use in other modules (if using modules)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initNavigation,
        initSmoothScrolling,
        initInteractiveElements,
        loadDynamicContent
    };
}