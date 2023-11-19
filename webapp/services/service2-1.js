document.getElementById('nextButton').addEventListener('click', function() {
    // Update progress bar
    let progressBar = document.getElementById('progressBar');
    let currentWidth = parseInt(progressBar.style.width, 10);
    progressBar.style.width = (currentWidth + 25) + '%';

    // Change content with an effect
    changeContent();
});

let currentStep = 0;
let content = [
    { title: "Take 5 min to answer to us", description: "We need to know more about you", question1: "Question 1", question2: "Question 2" },
    { title: "Take 5 min to answer to us", description: "We need to know more about you", question1: "Question 3", question2: "Question 4" },
    { title: "Take 5 min to answer to us", description: "We need to know more about you", question1: "Question 5", question2: "Question 6" },
    { title: "Take 5 min to answer to us", description: "We need to know more about you", question1: "Question 7", question2: "Question 8" },
    // Add more steps as needed
];

function changeContent() {
    let panel = document.querySelector('.questionnaire-left-panel-2');
    let predictionsDiv = document.querySelector('.predictions');

    if (currentStep < content.length) {
        // Supprimer la classe 'fade-in' avant d'ajouter 'fade-out'
        panel.classList.remove('fade-in');
        panel.classList.add('fade-out');
        
        // Attendre la fin de l'effet de fondu avant de changer le contenu
        setTimeout(() => {
            document.getElementById('questionnaireTitle').textContent = content[currentStep].title;
            document.getElementById('questionnaireDescription').textContent = content[currentStep].description;
            document.getElementById('labelQuestion1').textContent = content[currentStep].question1;
            document.getElementById('labelQuestion2').textContent = content[currentStep].question2;

            // Supprimer la classe 'fade-out' et ajouter 'fade-in'
            panel.classList.remove('fade-out');
            panel.classList.add('fade-in');
            currentStep++;
        }, 500); // Ajuster ce temps en fonction de la durée de votre effet de fondu
    } else {
        // Afficher les prédictions
        panel.classList.add('fade-out');
        setTimeout(() => {
            panel.style.display = 'none'; // Masquer le panneau de questions
            predictionsDiv.style.display = 'block'; // Afficher le panneau de prédictions
            predictionsDiv.classList.remove('fade-out');
            predictionsDiv.classList.add('fade-in'); // Appliquer l'effet de fondu en entrée
        }, 500);
    }
}
