from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Pour permettre les requêtes cross-origin (utile pour les applications web)

# Dictionnaire de réponses personnalisées
custom_responses = {
    "bonjour": ["Bonjour!", "Hello!", "Halo!", "Quetal?"],
    "ça va?": ["Ça va bien, merci!", "Je vais bien, et toi?", "Tout va bien!", "Ça roule!"],
    # Ajoutez d'autres messages et réponses personnalisées ici
}

@app.route('/')
def home():
    return "Bienvenue sur l'API de discussion IA."

@app.route('/api/respond', methods=['POST'])
def respond():
    data = request.get_json()
    user_message = data.get('message').lower()  # Convertir le message en minuscule pour une correspondance insensible à la casse

    if user_message in custom_responses:
        response = random.choice(custom_responses[user_message])
    else:
        response = "Je ne comprends pas ce message."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
