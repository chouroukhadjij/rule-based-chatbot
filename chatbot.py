"""
Projet 1 - Rule-Based AI Chatbot
DecodeLabs - Artificial Intelligence Track

Un chatbot simple qui répond à des questions prédéfinies
en utilisant un dictionnaire (base de connaissances) et une boucle continue.
"""

# --- 1. BASE DE CONNAISSANCES (Knowledge Base) ---
# Dictionnaire "question": "réponse". Facile à agrandir plus tard !
responses = {
    "hello": "Salut ! Comment puis-je t'aider aujourd'hui ?",
    "hi": "Hey ! Ravi de te parler.",
    "how are you": "Je vais très bien, merci de demander ! Et toi ?",
    "what is your name": "Je suis le chatbot officiel de DecodeLabs 🤖",
    "who made you": "J'ai été créé pendant le Projet 1 de l'Industrial Training Kit.",
    "what can you do": "Pour l'instant, je réponds juste à quelques questions simples !",
    "thank you": "Avec plaisir 😊",
    "thanks": "De rien !",
}

# Mots qui déclenchent la sortie du programme
exit_commands = ["exit", "bye", "quit", "au revoir"]


def clean_input(text):
    """Nettoie le texte : minuscules + suppression des espaces inutiles."""
    return text.lower().strip()


def get_response(user_input):
    """Cherche une réponse dans le dictionnaire, sinon renvoie une réponse par défaut."""
    return responses.get(user_input, "Désolé, je ne comprends pas cette phrase. 🤔")


def run_chatbot():
    print("=" * 50)
    print("🤖 Bienvenue sur le Rule-Based Chatbot de DecodeLabs")
    print("Tape 'exit' ou 'bye' pour quitter.")
    print("=" * 50)

    while True:  # boucle infinie = "heartbeat" du bot
        raw_input_text = input("\nToi : ")
        user_input = clean_input(raw_input_text)

        # Commande de sortie -> on casse la boucle proprement
        if user_input in exit_commands:
            print("Bot : À bientôt ! 👋")
            break

        # Sinon on cherche une réponse et on l'affiche
        reply = get_response(user_input)
        print("Bot :", reply)


# Point d'entrée du programme
if __name__ == "__main__":
    run_chatbot()
