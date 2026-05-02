import unittest
import os
from dotenv import load_dotenv

class TestAislamiento(unittest.TestCase):
    
    def setUp(self):
        """
        Se ejecuta ANTES de cada test
        """
        # Intentar cargar ambiente de testing, con fallback si no existe el archivo
        env_path = 'config/testing.env'
        if os.path.exists(env_path):
            load_dotenv(env_path)
        else:
            # Fallback para GitHub Actions: configurar variables manualmente
            os.environ['ENVIRONMENT'] = 'testing'
            os.environ['DB_HOST'] = 'localhost'
            os.environ['DB_NAME'] = 'mi_proyecto_test'
        
        self.datos_test = {'valor': 10}
        print(f"\n[SETUP] Ambiente: {os.getenv('ENVIRONMENT')}")
    
    def tearDown(self):
        """
        Se ejecuta DESPUÉS de cada test
        """
        self.datos_test = None
        print("[TEARDOWN] Limpieza completada")
    
    def test_01_suma(self):
        """Test independiente 1"""
        resultado = self.datos_test['valor'] + 5
        self.assertEqual(resultado, 15)
        print("[TEST 1] [OK] Suma correcta")
    
    def test_02_resta(self):
        """Test independiente 2 - NO depende del test 1"""
        resultado = self.datos_test['valor'] - 3
        self.assertEqual(resultado, 7)
        print("[TEST 2] [OK] Resta correcta")
    
    def test_03_aislamiento_datos(self):
        """Verificar que los datos se reinician en cada test"""
        # Cada test debe recibir datos frescos (valor = 10)
        self.assertEqual(self.datos_test['valor'], 10)
        print("[TEST 3] [OK] Datos aislados correctamente")

if __name__ == '__main__':
    unittest.main(verbosity=2)