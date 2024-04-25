import csv
import os
from Clase_Categorias import Categoria

class Gastos(Categoria):
    
    def __init__(self,monto,fecha,categoria,integrante):
        super().__init__(categoria)
        self.monto=monto
        self.fecha=fecha
        self.integrante=integrante
        self.leer_categorias()

    #Funcionalidad de regirar gastos, recibe el usuario actual al momento de escribir el gasto en el CSV herada el rol integrante
    def registro_Gasto(self,usuario_actual):

        print('Estas son las Categorias registradas actualmente')
        print(",".join(Categoria.lista_categorias))

        while True:
            try:
                self.categoria=input('Ingrese la categoria del Gasto: ').strip().capitalize()
                if self.categoria in Categoria.lista_categorias:
                    break
                else:
                    self.categoria not in Categoria.lista_categorias
                    print('La categoria seleccionada no esta registrada')
                    nuevo_registro=input('Desea registrar una nueva Categoria? Si/No: ').upper()
                    if nuevo_registro=="SI":
                        Categoria.registrar_categoria(self)
                        self.leer_categorias()
                    else:
                        break
            except ValueError:
                print('La categoria seleccionada no esta registrada')
        
        while True:
            try:
                self.monto= float(input('Ingrese el monto gastado: '))
                if self.monto >=0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede ingresar números negativos ni letras')

        while True:
            meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            try:
                self.fecha=input('Ingrese el mes del Gasto en formato de tres letras: ').capitalize()
                largo=len(self.fecha)
                if largo !=3 or not self.fecha.isalpha() or self.fecha not in meses:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Solo puede ingresar letras y no puede dejar el campo en blanco')

        with open("Gastos.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.fecha,self.categoria,self.monto,self.integrante])
    