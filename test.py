

import csv
def leer_Integrantes():
        with open("Integrantes.csv",mode="r",newline="") as archivoCSV:
            reader=csv.reader(archivoCSV,delimiter=",")
            header=next(reader)
            for fila in reader:
                  print(header)


leer_Integrantes()