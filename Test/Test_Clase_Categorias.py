import csv
import os
import unittest
from unittest.mock import patch
import io
import sys

from Clase_Categorias import Categoria

class TestCategoria(unittest.TestCase):
    def setUp(self):
        self.output = io.StringIO()
        sys.stdout = self.output

        with open('Categorias.csv', mode='w', newline='') as archivoCSV:
            pass

    def tearDown(self):
        sys.stdout = sys.__stdout__
        try:
            os.remove('Categorias.csv')
        except FileNotFoundError:
            pass

    def test_registrar_categoria(self):
        categoria = Categoria('internet')
        input_values = ['Carnes'] 
        input_iter = iter(input_values)

        def custom_input(prompt):
            return next(input_iter)

        with patch('builtins.input', custom_input):
            categoria.registrar_categoria()

        with open("Categorias.csv", mode="r") as archivoLecturaCSV:
            reader = csv.reader(archivoLecturaCSV, delimiter=",")
            data = list(reader)

        self.assertEqual(len(data), 1, "No son iguales")
        self.assertEqual(data[0][0], input_values[0])

    def test_registrar_categoria_con_duplicado_y_vacio(self):
        categoria = Categoria('')
        input_values = ['Carnes', ''] 
        input_iter = iter(input_values)

        def custom_input(prompt):
            try:
                value = next(input_iter)
                if value == '':
                    raise ValueError("No puede dejar este campo en blanco")
                return value
            except StopIteration:
                return ''


        self.output = io.StringIO()
        sys.stdout = self.output


if __name__ == '__main__':
    unittest.main()