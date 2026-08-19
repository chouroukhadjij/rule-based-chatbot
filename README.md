# 🤖 Rule-Based AI Chatbot

Un chatbot simple basé sur des règles (if-else / dictionnaire), développé dans le cadre du **Project 1 - Industrial Training Kit** chez **DecodeLabs**.

## 📌 Description

Ce projet est la première étape avant de plonger dans le Machine Learning et le Deep Learning. Avant de construire des systèmes qui *apprennent*, il faut d'abord maîtriser la logique de contrôle (**control flow**) et la prise de décision explicite.

Le bot répond à des questions prédéfinies grâce à un dictionnaire Python (recherche en temps constant O(1)), avec une réponse par défaut pour toute entrée inconnue.

## ✨ Fonctionnalités

- 🔁 Boucle continue (`while True`) pour une conversation en temps réel
- 🧹 Nettoyage automatique de l'input (minuscules + suppression des espaces)
- 📚 Base de connaissances sous forme de dictionnaire (facilement extensible)
- 🛡️ Réponse de secours (*fallback*) pour les entrées non reconnues
- 🚪 Commandes de sortie multiples (`exit`, `bye`, `quit`)

## 🛠️ Technologies

- Python 3

## 🚀 Installation & Utilisation

```bash
# Cloner le repo
git clone https://github.com/TON-USERNAME/rule-based-chatbot.git
cd rule-based-chatbot

# Lancer le chatbot
python chatbot.py
```

## 💬 Exemple d'utilisation

```
Toi : hello
Bot : Salut ! Comment puis-je t'aider aujourd'hui ?

Toi : what is your name
Bot : Je suis le chatbot officiel de DecodeLabs 🤖

Toi : bye
Bot : À bientôt ! 👋
```

## 📈 Prochaines étapes

- [ ] Ajouter la détection de mots-clés (au lieu d'une correspondance exacte)
- [ ] Ajouter plus d'intentions
- [ ] Passer à un chatbot basé sur des embeddings sémantiques (Project 2)

## 👤 Auteur

Projet réalisé dans le cadre du programme **DecodeLabs Industrial Training Kit 2026**.

---
⭐ N'hésite pas à laisser une étoile si ce projet t'a plu !
