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

# Liste de réponses par défaut pour les messages non reconnus
default_responses = [
    "Je ne sais pas.",
    "Désolé, je ne comprends pas.",
    "Peux-tu reformuler?",
    "Je ne suis pas sûr de ce que tu veux dire.",
    "Hmmm, je ne sais pas."
]

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
        response = random.choice(default_responses)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
