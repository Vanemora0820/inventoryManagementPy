from src.models.product import Product
from config import db

class ProductService:
    def get_all_products(self):
        products = Product.query.all()
        return [self.to_dict(product) for product in products]

    def add_product(self, data):
        if 'id' in data:
            data.pop('id')
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return self.to_dict(product)

    def to_dict(self, product):
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description
            
        }
