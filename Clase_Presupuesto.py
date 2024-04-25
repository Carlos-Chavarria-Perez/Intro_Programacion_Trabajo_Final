import csv
import os
import datetime


class Presupuesto:
    def __init__(self,presupuesto_mensual) -> None:
        self.presupuesto_mensaul=presupuesto_mensual
        self.arhivo_presupuesto='Presupuesto.csv'
    
    #Funcionaliad de definir un presupuesto, recive Usarios actual, ya que solo Padre, o Madre pueden modificar el presupuesto 
    def registrar_Presupuesto(self,integrante): 
        presuesto_actual=0

        if os.path.exists(self.arhivo_presupuesto):
            with open("Presupuesto.csv",mode="r",newline="") as archivoCSV:
                reader=csv.reader(archivoCSV,delimiter=",")
                for fila in reader:
                    presuesto_actual=fila[0]
                
        actualizar=input(f'Desea Actualizar el presupuesto Actual de {presuesto_actual} Si/No: ').upper()
        if actualizar=="SI":
            fecha=datetime.datetime.now()
            fecha_registro = fecha.strftime("%m/%Y")
            while True:
                try:
                    self.presupuesto_mensual=int(input('Ingrese el presupuesto del mes: ')) 
                    if self.presupuesto_mensual>0:
                        print(f'El presupuesto ha sido actualziado a {self.presupuesto_mensual}')
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('No puede ingresar un presupuesto negativo')

            with open("Presupuesto.csv",mode="a",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow([self.presupuesto_mensual,fecha_registro])
        