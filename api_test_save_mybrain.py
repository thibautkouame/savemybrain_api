from flask import Flask, request, jsonify
import random
import difflib

app = Flask(__name__)

# Dictionnaires de traduction avec regroupement de synonymes
translations_fr_to_dyu = {
    ("bonjour", "hey", "salut"): ["A' ni sɔgɔma","a ni sogôman, i ka kene wâ?", "a ni sogôman"],
    "merci": ["i ni ce", "i ni san"],
    "comment ça va": ["i ka kene", "i ka kene wa?"],
    # Ajoutez plus de traductions ici
}

translations_dyu_to_fr = {
    "a ni sogôman, i ka kene wâ?": ["bonjour", "hey", "salut"],
    "a ni sogôman": ["bonjour", "hey", "salut"],
    "i ni ce": ["merci"],
    "i ni san": ["merci"],
    "i ka kene": ["comment ça va"],
    "i ka kene wa?": ["comment ça va"],
    # Ajoutez plus de traductions ici
}

translations_fr_to_agni = {
    ("bonjour", "hey", "salut"): ["baba mo", "baba moho"],
    "merci": ["moho", "moho ho"],
    "comment ça va": ["eh", "eh ho"],
    # Ajoutez plus de traductions ici
}

translations_agni_to_fr = {
    "baba mo": ["bonjour", "hey", "salut"],
    "baba moho": ["bonjour", "hey", "salut"],
    "moho": ["merci"],
    "moho ho": ["merci"],
    "eh": ["comment ça va"],
    "eh ho": ["comment ça va"],
    # Ajoutez plus de traductions ici
}

translations_agni_to_dyu = {
    "baba mo": ["a ni sogôman, i ka kene wâ?", "a ni sogôman"],
    "baba moho": ["a ni sogôman, i ka kene wâ?", "a ni sogôman"],
    "moho": ["i ni ce", "i ni san"],
    "moho ho": ["i ni ce", "i ni san"],
    "eh": ["i ka kene", "i ka kene wa?"],
    "eh ho": ["i ka kene", "i ka kene wa?"],
    # Ajoutez plus de traductions ici
}

translations_dyu_to_agni = {
    "a ni sogôman, i ka kene wâ?": ["baba mo", "baba moho"],
    "a ni sogôman": ["baba mo", "baba moho"],
    "i ni ce": ["moho", "moho ho"],
    "i ni san": ["moho", "moho ho"],
    "i ka kene": ["eh", "eh ho"],
    "i ka kene wa?": ["eh", "eh ho"],
    # Ajoutez plus de traductions ici
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    source = data.get('source')
    target = data.get('target')

    def get_best_match(dictionary, text):
        all_keys = [key for key_group in dictionary.keys() for key in (key_group if isinstance(key_group, tuple) else (key_group,))]
        closest_matches = difflib.get_close_matches(text.lower(), all_keys, n=1, cutoff=0.5)
        if closest_matches:
            best_match = closest_matches[0]
            for key, values in dictionary.items():
                if best_match in (key if isinstance(key, tuple) else (key,)):
                    return random.choice(values)
        return "Traduction non trouvée"

    if source == 'fr' and target == 'dyu':
        translated_text = get_best_match(translations_fr_to_dyu, text)
    elif source == 'dyu' and target == 'fr':
        translated_text = get_best_match(translations_dyu_to_fr, text)
    elif source == 'fr' and target == 'agni':
        translated_text = get_best_match(translations_fr_to_agni, text)
    elif source == 'agni' and target == 'fr':
        translated_text = get_best_match(translations_agni_to_fr, text)
    elif source == 'agni' and target == 'dyu':
        translated_text = get_best_match(translations_agni_to_dyu, text)
    elif source == 'dyu' and target == 'agni':
        translated_text = get_best_match(translations_dyu_to_agni, text)
    else:
        return jsonify({'error': 'Langue source ou cible non supportée'}), 400
    
    return jsonify({'translatedText': translated_text})
