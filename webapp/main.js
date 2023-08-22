/* Effet défilement fluide */ 
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


/* section 2 feature et large-feature */ 
$(document).ready(function() {

  // Fonction pour gérer le comportement de clic sur .feature
  function handleFeatureClick() {
      var index = $(this).index();

      // Cachez tous les .large-feature en mettant leur opacité à 0
      $(".large-feature").css("opacity", "0");

      setTimeout(function() {
          $(".large-feature").hide();
          // Affichez seulement le .large-feature correspondant
          $(".large-feature").eq(index).show().css("opacity", "1");
      }, 200);

      // Retirez l'effet d'ombre de tous les .feature
      $(".feature").css("box-shadow", "none").removeClass('active');
      // Appliquez l'effet d'ombre seulement à la .feature cliquée et ajoutez la classe 'active'
      $(this).css("box-shadow", "0 4px 8px rgba(0, 0, 0, 0.1)").addClass('active');
  }

  // Attachez l'événement de clic
  $(".feature").click(handleFeatureClick);

  // Gérer le comportement de survol
  $(".feature").hover(
      function() {
          // Si la .feature n'est pas déjà active, changez son style lorsqu'elle est survolée
          if (!$(this).hasClass('active')) {
              $(this).css("box-shadow", "0 4px 8px rgba(0, 0, 0, 0.1)");
          }
      },
      function() {
          // Si la .feature n'est pas déjà active, remettez son style à la normale lorsqu'elle n'est plus survolée
          if (!$(this).hasClass('active')) {
              $(this).css("box-shadow", "none");
          }
      }
  );

  // Déclenchez un clic sur la première div .feature
  $(".feature").first().click();
});


/* section 3 service */ 
$(document).ready(function() {
  // Cliquez sur un service
  $(".service").on("click", function(e) {
      e.preventDefault(); // Empêche le comportement par défaut du lien

      $(".service.active").removeClass("active");
      $(this).addClass("active");

      var src = $(this).find('.service-logo').attr('src');
      displayEnlargedService(src);
  });

  // Affichage de l'image du service en grand
  function displayEnlargedService(src) {
    var leftSection = $(".left-section");
    var enlargedLogo = leftSection.find('.enlarged-service-logo');
  
    if (enlargedLogo.length > 0) {
      enlargedLogo.remove();
    }
  
    enlargedLogo = $('<img class="enlarged-service-logo animate">').appendTo(leftSection);
    enlargedLogo.attr('src', src).css('opacity', 0).show().animate({ opacity: 1 }, 500);
  }

  // Masquer l'image du service en grand lorsque vous cliquez sur un autre élément
  $(document).on('click', function(e) {
      if (!$(e.target).closest('.service').length && !$(e.target).closest('.left-section').length) {
          $(".left-section .enlarged-service-logo").fadeOut();
      }
  });

  // Survoler un service
  $(".service").hover(
      function() {
          if (!$(this).hasClass('active')) {
              $(this).addClass('hovered');
          }
      },
      function() {
          $(this).removeClass('hovered');
      }
  );
});

document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll('section[id]');

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      const id = entry.target.getAttribute('id');
      const navLink = document.querySelector(`nav ul li a[href="#${id}"]`);
      if (navLink) {  // Vérifie si le lien existe
        if (entry.isIntersecting) {
          navLink.classList.add('active');
        } else {
          navLink.classList.remove('active');
        }
      }
    });
  }, {
    // Trigger the callback at various intersection levels
    threshold: [0, 0.1, 0.25, 0.5, 0.75, 1]
  });

  sections.forEach(section => {
    observer.observe(section);
  });
});
