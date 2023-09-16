from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Chargement du modèle et du tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
chat_history_ids = None  # on initialise cela à l'extérieur pour conserver l'historique des échanges

@app.route('/get_response', methods=['POST'])
def get_response():
    global chat_history_ids
    user_input = request.json['text']

    # encoder l'input et ajouter le token EOS
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # concaténer l'input utilisateur avec l'historique de chat (s'il y en a)
    bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if chat_history_ids is not None else input_ids

    # générer une réponse du bot
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=0,
        temperature=0.75,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # obtenir la réponse
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
