from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import datetime, timedelta
import uuid
import bcrypt

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # à changer pour production

# Stockage temporaire des "pastes"
pastes = {}


# Définit une route pour la page d'accueil (/) qui accepte à la fois les méthodes HTTP GET et POST
@app.route('/', methods=['GET', 'POST'])
def index():  # Fonction associée à la route /
    if request.method == 'POST':  # Vérifie si le user soumet un formulaire
        # Récupère le contenu du champs content envoyé dans le formulaire de la requête
        content = request.form.get('content')
        print("Contenu :", content)
        if not content:
            # Message d'erreur si aucun contenu n'est founit
            return "Aucun contenu fourni", 400

        # Récupère le contenu du champs expire envoyé dans le formulaire de la requête (10 par défaut)
        expire_minutes = int(request.form.get('expire', 10))

        # Récupère le contenu du champs password envoyé dans le formulaire de la requête
        password = request.form.get('password')

        paste_id = str(uuid.uuid4())[:8]
        expire_at = datetime.utcnow() + timedelta(minutes=expire_minutes)

        hashed_pw = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()) if password else None

        pastes[paste_id] = {
            'content': content,
            'expire_at': expire_at,
            'password': hashed_pw
        }

        return redirect(url_for('view_paste', paste_id=paste_id))

    return render_template('index.html')


@app.route('/paste/<paste_id>', methods=['GET', 'POST'])
def view_paste(paste_id):
    paste = pastes.get(paste_id)

    if not paste or datetime.utcnow() > paste['expire_at']:
        pastes.pop(paste_id, None)
        return "Ce paste a expiré ou n'existe pas.", 404

    if paste['password']:
        if request.method == 'POST':
            input_pw = request.form.get('password', '').encode()
            if bcrypt.checkpw(input_pw, paste['password']):
                return render_template('paste.html', content=paste['content'], expire_at=paste['expire_at'].strftime("%Y-%m-%d %H:%M:%S"))
            else:
                flash("Mot de passe incorrect")
        return render_template('login.html', paste_id=paste_id)

    return render_template('paste.html', content=paste['content'])


if __name__ == '__main__':
    app.run(debug=True)
