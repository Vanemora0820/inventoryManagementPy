# Inventory Management System

## Descripción

Este es un sistema de gestión de inventario desarrollado en Python 3.12.4. El proyecto está diseñado para manejar la gestión de inventarios, con una estructura modular que separa las responsabilidades en diferentes capas: controladores, modelos y servicios.

## Estructura del Proyecto

El proyecto sigue la siguiente estructura de directorios:

inventory_management_py/
├── myenv/ # Entorno virtual
├── src/ # Código fuente
│ ├── controllers/ # Controladores para manejar las solicitudes
│ │ ├── init.py # Inicializador del módulo
│ │ └── inventory_controller.py # Lógica de manejo de inventario
│ ├── models/ # Modelos de datos
│ │ ├── init.py # Inicializador del módulo
│ │ └── inventory.py # Definición de los modelos de inventario
│ ├── services/ # Servicios de lógica de negocio
│ │ ├── init.py # Inicializador del módulo
│ │ └── inventory_service.py # Servicios relacionados con la gestión de inventario
│ ├── init.py # Inicializador del módulo
│ └── main.py # Punto de entrada de la aplicación



## Requisitos

- Python 3.12.4


## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Vanemora0820/inventoryManagementPy.git

 2.  Navega al directorio del proyecto:

 cd inventoryManagementPy

 3. Crea un entorno virtual y actívalo:

 python -m venv myenv
source myenv/bin/activate 
# En Windows usa 
`myenv\Scripts\activate`

4. Instala las dependencias si hay alguna en un archivo requirements.txt

pip install -r requirements.txt

5. Ejecuta

python src/main.py



