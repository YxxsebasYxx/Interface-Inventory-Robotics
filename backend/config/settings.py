import os

# Ruta al Excel de inventario
env_path = os.getenv('EXCEL_PATH', 'backend/data/inventory.xlsx')
EXCEL_PATH = env_path