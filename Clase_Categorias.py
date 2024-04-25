import csv
import os
import datetime

class Categoria:
    lista_categorias=[]
    def __init__(self,categoria) -> None:
        self.categoria=categoria

    #Class method para poder accer a la lista de Categrias
    @classmethod
    def leer_categorias(cls):
        cls.lista_categorias.clear()
        with open('Categorias.csv', mode="r") as archivoLecturaCSV:
            reader = csv.reader(archivoLecturaCSV, delimiter=",")
            try:
                next(reader)
            except StopIteration:
                print('El archivo esta vacío')

            for fila in reader:
                Categoria.lista_categorias.append(fila[0])

    #Funcionalidad de crear categorias
    def registrar_categoria(self):
        self.leer_categorias()
        while True:
            try:
                self.categoria=input('Ingrese la categoria que desea agregar: ').capitalize()
                if not self.categoria:
                    raise ValueError
                if self.categoria in Categoria.lista_categorias:
                    print('La categoria ya existe, no puede duplicar categorias')
                if self.categoria.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar este campo en blanco')

        with open("Categorias.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.categoria])
