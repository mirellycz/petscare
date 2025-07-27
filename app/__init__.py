from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secreto123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app





