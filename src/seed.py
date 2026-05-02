import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def seed_minimal_data():
    """
    Script de seed mínimo para poblar datos iniciales
    """
    print("=" * 50)
    print("SEED DE DATOS MINIMOS")
    print("=" * 50)
    print(f"Ambiente: {os.getenv('ENVIRONMENT')}")
    print(f"Base de datos: {os.getenv('DB_NAME')}")
    print(f"App: {os.getenv('APP_NAME')}")
    print()
    
    # Datos mínimos de ejemplo
    datos_iniciales = {
        'usuarios': [
            {'id': 1, 'nombre': 'Admin', 'email': 'admin@test.com'},
            {'id': 2, 'nombre': 'Tester', 'email': 'tester@test.com'}
        ],
        'configuracion': {
            'app_name': os.getenv('APP_NAME'),
            'version': os.getenv('APP_VERSION')
        }
    }
    
    print("Usuarios a crear:")
    for usuario in datos_iniciales['usuarios']:
        print(f"  - {usuario['nombre']} ({usuario['email']})")
    
    print()
    print("✓ Datos seed cargados exitosamente")
    print("=" * 50)
    
    return datos_iniciales

if __name__ == "__main__":
    seed_minimal_data()