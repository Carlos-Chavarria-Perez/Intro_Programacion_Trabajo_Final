import csv

class Gastos:
    
    def __init__(self, monto, fecha, categoria, integrante, categorias=None):
        self.monto = monto
        self.fecha = fecha
        self.categoria = categoria
        self.integrante = integrante
        self.categorias = categorias if categorias else []
        if not self.categorias:
            self.leer_categorias()

    def leer_categorias(self):
        try:
            with open('Categorias.csv', mode="r") as archivoLecturaCSV:
                reader = csv.reader(archivoLecturaCSV)
                for row in reader:
                    self.categorias.append(row[0])
        except FileNotFoundError:
            print("El archivo 'Categorias.csv' no se encuentra.")

    def registro_gasto(self, usuario_actual):
        pass