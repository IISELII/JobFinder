/* effet de défilement fluide avec JavaScript */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
      e.preventDefault();

      const target = document.querySelector(this.getAttribute('href'));

      if (target) {
          window.scrollTo({
              top: target.offsetTop - 50, // -50 pour ajuster la position si votre navigation a une hauteur
              behavior: 'smooth'
          });
      }
  });
});
