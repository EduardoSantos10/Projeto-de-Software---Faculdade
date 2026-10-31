import os
from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)

    # Segurança e Configuração via Environment Variables
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-ecobairro-2026-secure')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///ecobairro.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar rotas
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()  # Cria as tabelas SQLite automaticamente ao iniciar no MVP

    return app