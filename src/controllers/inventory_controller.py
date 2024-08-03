from flask import Blueprint, request, jsonify
from src.services.inventory_service import InventoryService

inventory_bp = Blueprint('inventory_bp', __name__)

service = InventoryService()

@inventory_bp.route('', methods=['GET'])
def get_inventory():
    inventories = service.get_all_inventory()
    return jsonify(inventories)

@inventory_bp.route('', methods=['POST'])
def add_inventory():
    data = request.json
    inventory = service.add_inventory(data)
    return jsonify(inventory), 201

@inventory_bp.route('/<int:id>/deliver', methods=['PATCH'])
def deliver_inventory(id):
    inventory = service.deliver_inventory(id)
    if inventory:
        return jsonify(inventory)
    return jsonify({'error': 'Inventario no disponible'}), 404
