import sys
sys.path.append('/d/Developer/Projects/inventory_management_py/src')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.inventory_controller import inventory_bp

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secreta@localhost:3306/inventary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Registrar el blueprint del controlador de inventario
app.register_blueprint(inventory_bp, url_prefix='/api/inventory')

if __name__ == '__main__':
    app.run(debug=True)

