$(document).ready(function() {
  // Lorsqu'un lien (a) est cliqué
  $('a[href^="#"]').on('click', function(e) {
    e.preventDefault();  // Empêche le comportement de navigation par défaut

    var target = $(this.hash);  // Obtient l'élément cible
    if (target.length) {
      // Défile doucement vers l'élément cible en 1000ms (1 seconde)
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 1000);  // Vous pouvez ajuster la durée (1000ms ici) pour rendre le défilement plus rapide ou plus lent
    }
  });
});
