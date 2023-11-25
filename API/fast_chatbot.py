from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, DPRQuestionEncoder, DPRQuestionEncoderTokenizer
import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Load Dense Passage Retrieval
# DPR_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
# DPR_model = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")

# Load the generator GPT-2 
tokenizer = AutoTokenizer.from_pretrained("ericzhou/DialoGPT-Medium-Rick_v2")
model = AutoModelForCausalLM.from_pretrained("ericzhou/DialoGPT-Medium-Rick_v2")
chat_history_ids = None  # Initialize to keep track of conversation history

@app.route('/')
def home():
    return "Chatbot API is running!"


@app.route('/get_response', methods=['POST'])
def get_response():
    global chat_history_ids
    user_input = request.json['text']

    # Encode the input and add the EOS token
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Concatenate user input with chat history (if any)
    bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if chat_history_ids is not None else input_ids
    
    # Generate a response from the bot
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=200,
        do_sample=True,
        top_p=0.85,
        top_k=40,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Retrieve the response
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    return jsonify({'response': response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)