import csv
import os
import datetime


class Presupuesto:
    def __init__(self,presupuesto_mensual) -> None:
        self.presupuesto_mensaul=presupuesto_mensual
        self.arhivo_presupuesto='Presupuesto.csv'
    
    def registrar_Presupuesto(self,integrante): 
        presuesto_actual=0

        if os.path.exists(self.arhivo_presupuesto):
            with open("Presupuesto.csv",mode="r",newline="") as archivoCSV:
                reader=csv.reader(archivoCSV,delimiter=",")
                for fila in reader:
                    presuesto_actual=fila[0]
                
        actualizar=input(f'Desea Actualizar el presupuesto Actual de {presuesto_actual} Si/No').upper()
        if actualizar=="SI":
            fecha=datetime.datetime.now()
            fecha_registro = fecha.strftime("%m/%Y")
            self.presupuesto_mensual=int(input('Ingrese el presupuesto del mes')) 
            with open("Presupuesto.csv",mode="a",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow([self.presupuesto_mensual,fecha_registro])