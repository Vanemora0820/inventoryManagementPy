from flask import Flask
from config import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secreta@localhost:3306/inventary'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from src.controllers.inventory_controller import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix='/api/inventory')

    return app
