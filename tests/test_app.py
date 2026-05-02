import unittest
import os
from dotenv import load_dotenv

class TestAislamiento(unittest.TestCase):
    
    def setUp(self):
        """
        Se ejecuta ANTES de cada test
        """
        # Cargar ambiente de testing
        load_dotenv('config/testing.env')
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
        self.assertEqual(resultado, 99)
        print("[TEST 1] ✓ Suma correcta")
    
    def test_02_resta(self):
        """Test independiente 2 - NO depende del test 1"""
        resultado = self.datos_test['valor'] - 3
        self.assertEqual(resultado, 7)
        print("[TEST 2] ✓ Resta correcta")
    
    def test_03_aislamiento_datos(self):
        """Verificar que los datos se reinician en cada test"""
        # Cada test debe recibir datos frescos (valor = 10)
        self.assertEqual(self.datos_test['valor'], 10)
        print("[TEST 3] ✓ Datos aislados correctamente")

if __name__ == '__main__':
    unittest.main(verbosity=2)