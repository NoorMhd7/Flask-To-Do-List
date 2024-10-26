document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.navbar-toggle');
    const navbar = document.querySelector('.navbar');

    toggle.addEventListener('click', () => {
        navbar.classList.toggle('active');
    });
});

