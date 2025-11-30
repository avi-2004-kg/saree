// Enhanced JavaScript for Kumudhini Silks website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all animations and interactions
    initScrollAnimations();
    initSmoothScroll();
    initContactForm();
    initImageGallery();
    initParallaxEffect();
});

// Smooth scrolling for navigation links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Intersection Observer for scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const animationElements = document.querySelectorAll(
        '.highlight-item, .collection-item, .value-item, .product-card, .assurance-item, .info-box, .contact-details'
    );

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.8s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animationElements.forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
}

// Enhanced contact form handling
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                subject: document.getElementById('subject').value,
                message: document.getElementById('message').value
            };

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                if (response.ok) {
                    const result = await response.json();
                    showNotification('Message sent successfully! We\'ll get back to you soon.', 'success');
                    contactForm.reset();
                } else {
                    showNotification('An error occurred. Please try again.', 'error');
                }
            } catch (error) {
                showNotification('Network error. Please try again.', 'error');
            }
        });
    }
}

// Image gallery functionality
function initImageGallery() {
    const images = document.querySelectorAll('.collection-image, .product-image');
    images.forEach(image => {
        image.addEventListener('mouseenter', function() {
            this.style.cursor = 'pointer';
            this.style.transform = 'scale(1.05)';
        });
        image.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
}

// Parallax effect for hero sections
function initParallaxEffect() {
    window.addEventListener('scroll', () => {
        const scrollPosition = window.pageYOffset;
        const heroSections = document.querySelectorAll('.hero, .about-hero, .products-hero, .catalogue-hero, .contact-hero');
        
        heroSections.forEach(hero => {
            const heroTop = hero.offsetTop;
            const heroHeight = hero.clientHeight;
            const windowHeight = window.innerHeight;
            
            if (scrollPosition < heroTop + heroHeight && scrollPosition + windowHeight > heroTop) {
                const offset = (scrollPosition - heroTop) * 0.5;
                hero.style.backgroundPosition = `center ${offset}px`;
            }
        });
    });
}

// Utility function to show notifications
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style the notification with better appearance
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '18px 24px',
        borderRadius: '8px',
        color: 'white',
        fontWeight: '700',
        zIndex: '9999',
        boxShadow: '0 8px 24px rgba(42, 24, 16, 0.3)',
        fontSize: '1rem',
        animation: 'slideInRight 0.4s ease-out',
        fontFamily: "'Raleway', sans-serif"
    });
    
    // Set colors based on type
    const colors = {
        'success': { bg: '#4caf50', border: '2px solid #45a049' },
        'error': { bg: '#f44336', border: '2px solid #da190b' },
        'warning': { bg: '#ff9800', border: '2px solid #e68900' },
        'info': { bg: '#2196F3', border: '2px solid #0b7dda' }
    };

    const color = colors[type] || colors['info'];
    notification.style.backgroundColor = color.bg;
    notification.style.border = color.border;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 4 seconds with fade animation
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.4s ease-out forwards';
        setTimeout(() => notification.remove(), 400);
    }, 4000);
}

// Export for use in other scripts
window.showNotification = showNotification;

// Add animation keyframes dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideOutRight {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100px);
        }
    }
`;
document.head.appendChild(style);