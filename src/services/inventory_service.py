# src/services/inventory_service.py
from src.models.inventory import Inventory
from src.main import db

class InventoryService:
    def get_all_inventory(self):
        inventories = Inventory.query.all()
        return [inventory.__dict__ for inventory in inventories]

    def add_inventory(self, data):
        inventory = Inventory(**data)
        db.session.add(inventory)
        db.session.commit()
        return inventory.__dict__

    def deliver_inventory(self, id):
        inventory = Inventory.query.get(id)
        if inventory:
            inventory.status = 'Delivered'
            db.session.commit()
            return inventory.__dict__
        return None
