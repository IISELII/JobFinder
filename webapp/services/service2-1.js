document.getElementById('nextButton').addEventListener('click', function() {

    let progressBar = document.getElementById('progressBar');
    let totalSteps = content.length;
    let progressPercentage = ((currentStep + 1) / totalSteps) * 100 -25; 
    progressBar.style.width = progressPercentage + '%';

    

    changeContent();
});

// Ajouter un gestionnaire d'événements pour le bouton "RETAKE TEST"
document.getElementById('retakeButton').addEventListener('click', function() {

    currentStep = 0;

    let progressBar = document.getElementById('progressBar');
    progressBar.style.width = '0%';

    let panel = document.querySelector('.questionnaire-left-panel-2');
    panel.style.display = 'flex'; 
    resetContent();

    let predictionsDiv = document.querySelector('.predictions');
    predictionsDiv.style.display = 'none';
});

let currentStep = 0;
let content = [
    { title: "Take 5 min to answer us", description: "We need to know more about you", question1: "Quels tâches aimerais-tu faire dans un job ?"},
    { title: "Take 5 min to answer us", description: "We need to know more about you", question1: "Qualités", question2: "Diplômes ?" },
    { title: "Take 5 min to answer us", description: "We need to know more about you", question1: "Expériences", question2: "Compétences techniques ?" },
];

let progressBar = document.getElementById('progressBar');
progressBar.style.width = '0%';


function changeContent() {
    let panel = document.querySelector('.questionnaire-left-panel-2');
    let questionsContainer = document.querySelector('.questions-container');
    let predictionsDiv = document.querySelector('.predictions');

    if (currentStep < content.length) {
        panel.classList.remove('fade-in');
        panel.classList.add('fade-out');

        setTimeout(() => {
            document.getElementById('questionnaireTitle').textContent = content[currentStep].title;
            document.getElementById('questionnaireDescription').textContent = content[currentStep].description;

            // Nettoyer les champs précédents
            questionsContainer.innerHTML = '';

            // Créer de nouveaux champs de saisie pour chaque question
            Object.keys(content[currentStep]).forEach(key => {
                if (key.startsWith('question')) {
                    let questionDiv = document.createElement('div');
                    questionDiv.className = 'question';

                    let label = document.createElement('label');
                    label.htmlFor = key;
                    label.textContent = content[currentStep][key];

                    let input = document.createElement('input');
                    input.type = 'text';
                    input.id = key;
                    input.placeholder = 'Enter your answer';

                    questionDiv.appendChild(label);
                    questionDiv.appendChild(input);
                    questionsContainer.appendChild(questionDiv);
                }
            });

            panel.classList.remove('fade-out');
            panel.classList.add('fade-in');
            currentStep++;

        }, 500); 
    } else {
        panel.classList.add('fade-out');
        setTimeout(() => {
            panel.style.display = 'none'; 
            predictionsDiv.style.display = 'block'; 
            predictionsDiv.classList.remove('fade-out');
            predictionsDiv.classList.add('fade-in'); 
        }, 500);
    }
}

function sendToAPI() {
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userResponses),
    })
    .then(response => response.json())
    .then(data => {
        updatePredictions(data.prediction);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function updatePredictions(predictions) {
    let predictionDiv = document.querySelector('.job-prediction');
    predictionDiv.textContent = predictions[0]; 
}

// Fonction pour réinitialiser le contenu du questionnaire
function resetContent() {
    document.getElementById('questionnaireTitle').textContent = content[0].title;
    document.getElementById('questionnaireDescription').textContent = content[0].description;

    changeContent();
}


// On appelle changeContent pour charger la première question
changeContent();
