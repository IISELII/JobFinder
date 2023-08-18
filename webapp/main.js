function fetchJobRecommendations() {
    let query = document.getElementById("jobQuery").value;

    // Appelez ici votre API avec la requête de l'utilisateur (ici, je simule une réponse)
    let jobRecommendations = ["Développeur", "Designer", "Chef de projet"];  // Simulé, à remplacer par la réponse de votre API

    let resultsDiv = document.getElementById("jobResults");
    resultsDiv.innerHTML = jobRecommendations.join(", ");
}
