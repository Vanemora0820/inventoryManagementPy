# src/controllers/inventory_controller.py
from flask import Blueprint, request, jsonify
from src.services.inventory_service import InventoryService

inventory_bp = Blueprint('inventory_bp', __name__)
inventory_service = InventoryService()

@inventory_bp.route('/', methods=['GET'])
def get_all_inventory():
    inventories = inventory_service.get_all_inventory()
    return jsonify(inventories), 200

@inventory_bp.route('/', methods=['POST'])
def add_inventory():
    data = request.get_json()
    inventory = inventory_service.add_inventory(data)
    return jsonify(inventory), 201

@inventory_bp.route('/<int:id>/deliver', methods=['PUT'])
def deliver_inventory(id):
    inventory = inventory_service.deliver_inventory(id)
    if inventory:
        return jsonify(inventory), 200
    return jsonify({'message': 'Inventory not found'}), 404

