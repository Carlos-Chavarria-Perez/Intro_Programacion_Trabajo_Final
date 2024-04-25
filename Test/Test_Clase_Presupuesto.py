import csv
import unittest
from unittest.mock import patch

class Presupuesto:
    def __init__(self, presupuesto_mensual) -> None:
        self.presupuesto_mensual = presupuesto_mensual
    
    def registrar_Presupuesto(self): 
        presupuesto_actual = 0
        
        actualizar = input(f'Desea Actualizar el presupuesto Actual de {self.presupuesto_mensual} Si/No').upper()
        if actualizar == "SI":
            self.presupuesto_mensual = int(input('Ingrese el presupuesto del mes')) 

class TestPresupuesto(unittest.TestCase):
    def setUp(self):
        self.presupuesto = Presupuesto(1000)

    @patch('builtins.input', side_effect=['SI', '2000'])
    def test_registrar_Presupuesto_si(self, mock_input):
        self.presupuesto.registrar_Presupuesto()
        self.assertEqual(self.presupuesto.presupuesto_mensual, 2000)

    @patch('builtins.input', side_effect=['NO'])
    def test_registrar_Presupuesto_no(self, mock_input):
        self.presupuesto.registrar_Presupuesto()
        self.assertEqual(self.presupuesto.presupuesto_mensual, 1000)

if __name__ == "__main__":
    unittest.main()