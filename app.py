from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
import os
from config import config

app = Flask(__name__)

# Configuración basada en variable de entorno
config_name = os.environ.get('FLASK_ENV', 'default')
app.config.from_object(config[config_name])

# Inicializar extensiones
from models import db, bcrypt
db.init_app(app)
bcrypt.init_app(app)

# Importar modelos después de inicializar db
from models import User, Idea, Team

# Importar rutas
from routes.auth_routes import auth_routes
from routes.idea_routes import idea_routes
from routes.user_routes import user_routes
from routes.team_routes import team_routes
from routes.admin_routes import admin_bp

# Registrar blueprints
app.register_blueprint(auth_routes)
app.register_blueprint(idea_routes)
app.register_blueprint(user_routes)
app.register_blueprint(team_routes)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Permitir acceso desde otros dispositivos en la red local
    app.run(debug=True, host='0.0.0.0', port=5000)
