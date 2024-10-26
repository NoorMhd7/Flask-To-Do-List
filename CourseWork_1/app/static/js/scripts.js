document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.navbar-toggle');
    const navbar = document.querySelector('.navbar');

    toggle.addEventListener('click', () => {
        navbar.classList.toggle('active');
    });
});

// scripts.js for create.html

document.addEventListener("DOMContentLoaded", function() {
    const formContainer = document.querySelector('.form-container');
    formContainer.style.opacity = 0;
    formContainer.style.transition = 'opacity 0.5s ease-in-out';
    setTimeout(() => {
        formContainer.style.opacity = 1;
    }, 100);
});
