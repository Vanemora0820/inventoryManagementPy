import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import create_app

app = create_app()

# Ruta para la página principal
@app.route('/')
def index():
    return "Bienvenido a la API de Gestión de Inventario"

if __name__ == '__main__':
    app.run(debug=True)
