$(document).ready(function() {
    // Fonction pour envoyer le message
    function sendMessage() {
        const userMessage = $("#chat-input").val();
        const conversationsDiv = $("#conversations");

        if (userMessage.trim() !== "") {
            // Afficher le message de l'utilisateur
            conversationsDiv.append(`<div class="user-message">${userMessage}</div>`);

            // Désactiver le bouton pendant la requête
            $("#send-btn").prop("disabled", true);

            // Envoi du message à l'API
            $.ajax({
                type: "POST",
                url: "http://localhost:5000/get_response",
                data: JSON.stringify({ text: userMessage }),
                contentType: "application/json",
                dataType: "json",
                success: function(data) {
                    let botResponse = data.response || "Désolé, je n'ai pas pu traiter votre demande.";

                    // Créer un élément pour la réponse du bot
                    let botMessageElement = $('<div class="bot-message"></div>');
                    conversationsDiv.append(botMessageElement);

                    // Effet d'écriture progressive
                    let i = 0;
                    let interval = setInterval(function() {
                        if (i < botResponse.length) {
                            botMessageElement.append(botResponse[i]);
                            i++;
                        } else {
                            clearInterval(interval);
                        }
                    }, 50); // 50ms pour chaque caractère
                },
                error: function(xhr, status, error) {
                    console.error("Erreur lors de la requête:", status, error);
                    conversationsDiv.append('<div class="bot-message">Désolé, une erreur est survenue. Veuillez réessayer plus tard.</div>');
                },
                complete: function() {
                    // Réactiver le bouton une fois la requête terminée
                    $("#send-btn").prop("disabled", false);
                }
            });

            // Vider l'input
            $("#chat-input").val("");
        }
    }

    // Événement click pour le bouton d'envoi
    $("#send-btn").on("click", sendMessage);

    // Événement pour la touche "Enter"
    $("#chat-input").on("keypress", function(e) {
        if (e.which === 13) {
            sendMessage();
        }
    });
});