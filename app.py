# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    # 👇 Import models so Alembic can discover them
    from models import User, Bus, Booking  # include all your models here

    from routes.auth_routes import auth_bp
    from routes.bus_routes import bus_bp
    from routes.booking_routes import booking_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(bus_bp)
    app.register_blueprint(booking_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
