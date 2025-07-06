==========================
Chatbot API avec Django + GroqCloud
==========================

Prérequis :
-----------
- Python 3.x et pip installés
- Docker & Docker Compose installés (optionnel si tu utilises Docker)
- Clé API GroqCloud (https://app.groq.com)

Installation & lancement :
--------------------------
1. Cloner le projet :
   git clone https://github.com/toncompte/tonprojet.git
   cd tonprojet

2. (Option Docker) Construire et démarrer les conteneurs Docker :
   docker-compose build
   docker-compose up -d

3. (Si pas Docker) Installer les dépendances Python :
   python -m venv venv
   source venv/bin/activate    # ou venv\Scripts\activate sous Windows
   pip install -r requirements.txt

4. Configurer la clé GroqCloud en local :
   - Sous Linux/macOS :
     export GROQ_API_KEY="gsk_ta_clef_groqcloud"
   - Sous Windows (PowerShell) :
     setx GROQ_API_KEY "gsk_ta_clef_groqcloud"

5. Appliquer les migrations Django :
   python manage.py migrate

6. Créer un super utilisateur Django (optionnel) :
   python manage.py createsuperuser

7. Lancer le serveur Django :
   python manage.py runserver

8. Accéder à l'API :
   http://localhost:8000

Notes :
-------
- Le dossier `backend/venv` est local, à ignorer dans git.
- Si tu utilises Docker, MySQL et MongoDB sont configurés dans docker-compose.
- Pour utiliser GroqCloud, n'oublie pas de fournir ta clé API via la variable d'environnement.

Support :
---------
Pour toute question, ouvre une issue sur le dépôt GitHub.

---
Bonne chance et bon développement !
