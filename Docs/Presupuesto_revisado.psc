Algoritmo Presupuesto
	Escribir 'Bienvenido al archivo gastos familia'
	Escribir 'Ingrese Usuario'
	Leer usuario
	Escribir 'ingrese Contraseña'
	Leer CONTRASENA
	verificar <- Verdadero
	Mientras verificar=Verdadero Hacer
		Escribir 'Bienvenido ', usuario
		Si crear_archivo_Usuarios=falso Entonces
			Crear_archivo_familiares <- Abrir_archivo_familiares
		SiNo
			Escribir 'Ya existe archivo familiares'
		FinSi
		Si Crear_archivo_gastos=falso Entonces
			Crear_archivo_gastos <- Abrir_archivo_gastos
			lista_gastos <- crear_lista_gastos
		SiNo
			Escribir 'Ya existe archivo gastos'
		FinSi
		Si Crear_archivo_usuario=falso Entonces
			crear_archivo_Usuarios <- crear_arvhico_Usuarios
			lista_usuarios <- Crea_lista_usuarios
		SiNo
			Escribir 'Archivo Usuarios ya existe'
		FinSi
		Si crear_archivo_categorias Entonces
			crear_archivo_categorias <- crear_arvhivo_categorias
			lista_Categorias <- crear=lista_Categorias
		SiNo
			Escribir 'Archivo Categorias ya exsite'
		FinSi
		Escribir 'Desea registrar Usuario? Si/no'
		Leer respuesta
		Si Mayusculas(respuesta)='SI' Entonces
			Escribir 'Defina Su usuario'
			Leer usuario
			Mientras usuario<>lista_usuarios Hacer
				Escribir 'Ingrese Contraseña'
				Leer CONTRASENA2
				Escribir 'Ingrese el rol familiar'
				Leer Familiar
				Escribir 'Nombre del familiar'
				Leer nombre_familiar
				Escribir 'Apellido del familiar'
				Leer Apellido_familiar
				Escribir 'Edad del familiar'
				Leer edad_familiar
				Escribir 'Ingrese el género'
				Leer genero_familiar
				Escribir 'Familiar registrado correctamente'
				lista_usuarios <- usuario
			FinMientras
			Escribir 'Usuario registrado'
		SiNo
			Escribir 'No se ingresa nuevo usuario'
		FinSi
		Escribir 'Desear ingresar un nuevo gasto Si/no'
		Leer nuevo_gasto
		Si Minusculas(nuevo_gasto)='si' Entonces
			Escribir 'ingrese categoria del gasto'
			Leer categoria
			Escribir 'nombre gasto'
			Leer nombre_gasto
			Escribir 'fecha Gasto'
			Leer fecha_gasto
			Escribir 'cantidad del gasto'
			Leer monto_gasto
			Escribir 'quien hizo el gasto'
			Leer intregrante_gasto
		SiNo
			Escribir 'No se ingresa nuevo gasto'
		FinSi
		Escribir 'Desea consultar gasto por fecha si/no?'
		Leer consultar_gasto_fecha
		Si Minusculas(consultar_gasto_fecha)='si' Entonces
			fecha <- fecha_gasto
			categoria <- categoria
			gasto <- nombre_gasto
			monto_gastado <- monto
		SiNo
			Escribir 'No se consulta por fecha'
		FinSi
		Escribir 'Desea consultar algun gasto por miembro'
		Leer consultar_gasto_por_miembro
		Si Minusculas(consultar_gasto_por_miembro)='si' Entonces
			Escribir 'Nombre del miembro'
			Leer nombre_miembro
			Escribir 'Ingrese el gasto'
			Leer nombre_gasto
			Escribir 'Ingrese la fecha del gasto'
			Leer fecha_gasto
			Escribir 'Ingrese el monto del gasto'
			Leer monto_gasto
		SiNo
			Escribir 'No se encuentra al miembro'
		FinSi
		Escribir 'Desea consultar la categoria si/no?'
		Leer consultar_categoria
		Si Minusculas(consultar_categoria)='si' Entonces
			Escribir 'Nombre de la categoria'
			Leer nombre_categoria
		SiNo
			Escribir 'No se consulta categoria'
		FinSi
		Escribir 'Desea salir de archivos gastos familia? si/no'
		Leer verificar1
		Si Minusculas(verificar1)='si' Entonces
			verificar <- falso
		SiNo
			verificar <- falso
		FinSi
	FinMientras
	Escribir 'Gracias por su registro'
FinAlgoritmo
