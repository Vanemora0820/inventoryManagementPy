from sqlalchemy import inspect
from src.main import app, db

with app.app_context():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("Estas son mis tablas:", tables)

