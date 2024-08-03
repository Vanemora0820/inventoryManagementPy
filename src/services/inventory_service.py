from src.models.inventory import Inventory
from config import db

class InventoryService:
    def get_all_inventory(self):
        inventories = Inventory.query.all()
        return [self.to_dict(inventory) for inventory in inventories]

    def add_inventory(self, data):
        if 'id' in data:
            data.pop('id')
        inventory = Inventory(**data)
        db.session.add(inventory)
        db.session.commit()
        return self.to_dict(inventory)

    def deliver_inventory(self, id):
        inventory = Inventory.query.get(id)
        if inventory:
            inventory.status = 'Entregado'
            db.session.commit()
            return self.to_dict(inventory)
        return None

    def to_dict(self, inventory):
        return {
            'id': inventory.id,
            'quantity': inventory.quantity,
            'serial_number': inventory.serial_number,
            'status': inventory.status,
            'product_id': inventory.product_id,
            'user_id': inventory.user_id,
            'date': inventory.date.isoformat() if inventory.date else None
        }
