from flask import Blueprint, request, jsonify
from src.services.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)
service = ProductService()

@product_bp.route('', methods=['GET'])
def get_all_products():
    products = service.get_all_products()
    return jsonify(products), 200

@product_bp.route('', methods=['POST'])
def add_product():
    data = request.get_json()
    product = service.add_product(data)
    return jsonify(product), 201
