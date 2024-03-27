
import csv
import os
import datetime

class Persona:
    def __init__(self,nombre,apellido,edad) -> None:
        self.nombre=nombre
        self.apellido= apellido
        self.edad=edad

class Integrante(Persona):
    def __init__(self, nombre, apellido, edad,integrante) -> None:
        super().__init__(nombre, apellido, edad)
        self.integrante=integrante
    
    def reistro_Integrante(self):
        while True:
            try:
                self.nombre=input('Ingrese el nombre del miemrbo: ').strip()
                if self.nombre.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar el campo en blanco solo puede ingresar letras')
        while True:
            try:
                self.apellido=input("Ingrese el apellido del cliente: ")
                if self.apellido.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar el campo en blanco solo puede ingresar letras')
        while True:
            try:
                self.edad=int(input('Ingrese la edad:'))
                if self.edad >0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('La edad no puede ser 0 o menor a cero, tampoco puede ingresar letras o dejar el campo en blanco')
        while True:
            try:
                self.integrante=input('Ingrese el rol que desea asignarle a esta persona: ')
                if self.integrante.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede dejar el campo en blanco solo puede ingresar letras')
        
        with open("Integrantes.csv",mode="a",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow([self.nombre,self.apellido,self.edad,self.integrante])
    
    def leer_Integrantes(self):
        with open("Integrantes.csv",mode="r",newline="") as archivoCSV:
            reader=csv.reader(archivoCSV,delimiter=",")
            header=next(reader)
            print("Detalles de los Integrantes:")
            for fila in reader:
                for header_item,detalle in zip(header,fila):
                    print(f'{header_item}:{detalle}')


class Presupuesto:
    def __init__(self,presupuesto_mensual) -> None:
        self.presupuesto_mensaul=presupuesto_mensual
        self.arhivo_presupuesto='Presupuesto.csv'
    
    def registrar_Presupuesto(self): #agregar quien cambia presupuesto
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


class Categoria:
    lista_categorias=[]
    def __init__(self,categoria) -> None:
        self.categoria=categoria

    def registrar_categoria(self):

        with open('Categorias.csv', mode="r") as archivoLecturaCSV:
            reader = csv.reader(archivoLecturaCSV, delimiter=",")
            next(reader)  
            for fila in reader:
                Categoria.lista_categorias.append(fila[0])

        while True:
            try:
                self.categoria=input('Ingrese la categoria que desea agregar').capitalize()
                if not self.categoria:
                    raise ValueError
                if self.categoria in Categoria.lista_categorias:
                    print('La categoria ya existe, no puede duplicar categorias')
                else:
                    break
            except ValueError:
                print('No puede dejar este campo en blanco')

        with open("Categorias.csv",mode="a",newline="") as archivoCSV:
            writer=csv.writer(archivoCSV,delimiter=",")
            writer.writerow([self.categoria])

class Gastos(Categoria):
    
    def __init__(self,monto,fecha,categoria,integrante) -> None:
        super().__init__(categoria)
        self.monto=monto
        self.fecha=fecha
        self.integegrante=integrante

    def registro_Gasto(self):
        
        while True:
            try:
                self.monto= float(input('Ingrese el monto gastado: '))
                if self.monto >=0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('No puede ingresar numeros negativos ni letras')
        while True:
            try:
                self.fecha=input('Ingrese el mes del Gasto en formato de tres letras: ')
                largo=len(self.fecha)
                if largo >3:
                    print('Ese formato de mes no es valido')
                else:
                    break
            except ValueError:
                print('No puede ingresar numeros')
        while True:
            try:
                self.lista_categorias
                nuevo_gasto=input(f'Seleccion la categoria de gasto{Categoria.lista_categorias}')## ver porque no llama a la lista debeo instanciarlo?
                break
            except ValueError:
                print('Esa no es una cateogria valida')
class Sistema_Presupuesto:

    def __init__(self) -> None:
        self.arhivo_presupuesto='Presupuesto.csv'
        self.archivo_integrantes='integrantes.csv'
        self.arhivo_gastos='Gastos.csv'
        self.archivo_categorias='Categorias.csv'

    def creacion_arvhivo_Presupuesto(self):
        if not os.path.exists(self.arhivo_presupuesto):
            with open("Presupuesto.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Presupuesto','Fecha de Modificacion'])
    
    def creacion_archivo_Gastos(self):
        if not os.path.exists(self.arhivo_gastos):
            with open("Gastos.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Fecha','Categoria','Total Gastado','integrante'])

    def creacion_archivo_integrantes(self):
        if not os.path.exists(self.archivo_integrantes):
            with open("Integrantes.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Nombre','Edad','Integrante'])

    
    def creacion_archivo_Categorias(self):
        if not os.path.exists(self.archivo_categorias):
            with open("Categorias.csv",mode="w",newline="") as archivoCSV:
                writer=csv.writer(archivoCSV,delimiter=",")
                writer.writerow(['Categoria'])

    print('Bienvenido a su sistema de Presupuesto Mensual')
 
    def ejecutar(self):
        self.creacion_arvhivo_Presupuesto()
        self.creacion_archivo_integrantes()
        self.creacion_archivo_Categorias()
        self.creacion_archivo_Gastos()

        lista_opciones=[1,2,3,4,5,6]
        salir="NO"
        while salir=="NO":
            print('''Seleccione que desear realizar hoy
                1) Definir Presupuesto
                2) Ingresar un nuevo integrante
                3) Consultar integrantes Actuales
                4) Ingresar un nuevo gasto
                5) Ingresar una nueva categoria de gasto
                6) Mostrar resumen de gastos
                ''')

            while True:
                try:
                    opcion=int(input('Eliga un opcion'))
                    if opcion in lista_opciones:
                        break
                    else:
                        print('La opcion seleccionada no es valida, vuelvalo a intentar')
                except ValueError:
                    print('Solo puede ingresar numeros')
            
            if opcion==1:
                presupuesto1=Presupuesto("")
                presupuesto1.registrar_Presupuesto()
            if opcion==2:
                integrante1=Integrante("","","","")
                integrante1.reistro_Integrante()
            if opcion==3:
                integrante1=Integrante("","","","")
                integrante1.leer_Integrantes()
            if opcion==4:
                gasto1=Gastos("","","","")
                gasto1.registro_Gasto()
            if opcion==5:
                categoria1=Categoria("")
                categoria1.registrar_categoria()
            if opcion==6:
                pass
            salir=input('Desea salir del programa de presuspuesto Si/No?').upper()



sistemaPresupuesto = Sistema_Presupuesto()
sistemaPresupuesto.ejecutar()

print(Categoria.lista_categorias)