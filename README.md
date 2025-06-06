# 🧩 PasteVault — Partage sécurisé de messages temporaires

**PasteVault** est une application web minimaliste et sécurisée développée avec **Flask**. Elle permet de créer des messages secrets accessibles par lien, avec une **expiration automatique** et une **protection par mot de passe** (facultative). Idéale pour échanger des informations sensibles de manière éphémère.

---

## 🚀 Fonctionnalités

- 🔐 Création d’un **message secret** avec délai d’expiration (ex. 5 min)
- 🧂 Mot de passe optionnel, **chiffré avec bcrypt**
- 🔗 Génération d’un **lien unique**
- ⏳ Compte à rebours avant expiration visible pour l’utilisateur
- 💣 Destruction automatique après expiration
- 🖤 Interface intuitive et sombre (dark cyber style)
- 🧪 Messages flash pour l’UX (erreurs, validation...)

---

## 🎯 Cas d’usage

> Alice veut envoyer à Bob un mot de passe temporaire.  
Elle génère un message sur PasteVault, définit un mot de passe et une expiration de 5 minutes.  
Elle envoie à Bob le lien.  
Bob clique, entre le mot de passe, et lit le message.  
Après 5 minutes, le message s’autodétruit.

---

## 🛠️ Tech Stack

- **Backend** : Python 3, Flask
- **Frontend** : HTML5, CSS3, Dark UI (custom)
- **Sécurité** : Bcrypt, UUID, expiration en UTC
- **Sessions / Routes dynamiques / Redirection / Flash**

---

## 🧪 Aperçu

> *(Ajoute une capture ici quand possible)*

---

## 🔧 Installation rapide

```bash
# 1. Cloner le dépôt
git clone https://github.com/ton-utilisateur/pastevault.git
cd pastevault

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python app.py

# Accès à l'application : http://localhost:5000
#   S e c u r e - P a s t e  
 