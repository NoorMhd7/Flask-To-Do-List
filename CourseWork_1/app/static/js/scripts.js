// toggle button
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.navbar-toggle');
    const navbar = document.querySelector('.navbar');

    toggle.addEventListener('click', () => {
        navbar.classList.toggle('active');
    });
});

// scripts.js for create.html
document.addEventListener("DOMContentLoaded", function() {
    const formContainer = document.querySelector('.form-container, .assessment-container', );
    formContainer.style.opacity = 0;
    formContainer.style.transition = 'opacity 0.5s ease-in-out';
    setTimeout(() => {
        formContainer.style.opacity = 1;
    }, 100);
});

// flash messages time out
window.onload = function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    setTimeout(() => {
        flashMessages.forEach(message => {
            message.style.opacity = '0'; // Fade out
        });
    }, 2000); // 2000ms = 2 seconds

    // Completely remove the messages from the DOM after the fade-out transition
    setTimeout(() => {
        flashMessages.forEach(message => {
            message.remove();
        });
    }, 2500); // 500ms after fade out ends
};
