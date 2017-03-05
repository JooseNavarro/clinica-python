# -- encoding: utf-8

import mysql.connector
import sys
import os

def menu():

	sw = 0

	while sw==0:
		print ("Menu de consultorio")
		print("1. Ver consultorio. \n2. Agregar consultorio. \n3.Editar Consultorio. \n4.Eliminar Consultorio \n5.salir \n\n" )

		opcion = int(input("Ingrese una opcion: "))
		if opcion == 1:
			verConsultorio()
		elif opcion == 2:
			AgregarConsultorio()
		elif opcion == 3:
			editarConsultorio()
		elif opcion == 4:
			eliminarConsultorio()
		elif opcion == 5:
			print("Has salido del menu de consultorio")
			sw = 1
		else:
			print("opcion no valido, favor elegir una opcion valido\n")

def verConsultorio():

	os.system('cls')

	print("Consultorio")

	con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='clinica')
	cursor = con.cursor()

	cursor.execute("SELECT * FROM consultorio")

	rows = cursor.fetchall()

	for row in rows:
		print(row)

	cursor.close()
	con.close()


def AgregarConsultorio():

	os.system('cls')

	print("Agregar consultorio")

	con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='clinica')
	cursor = con.cursor()

	codigo = str(input("codigo: "))
	consultorio = str(input("consultorio: "))

	cursor.execute("INSERT INTO consultorio values ('"+codigo+"', '"+consultorio+"')")

	con.commit()
	cursor.close()
	con.close()


def eliminarConsultorio(): #modificar esto

	os.system('cls')

	print("Eliminar consultorio")

	con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='clinica')
	cursor = con.cursor()

	codigo = str(input("codigo: "))

	print("Esta seguro que desea elimiar este consultorio de codigo " + codigo + ": (1=Si / 2=No)")

	if op == 1:
		try:
			cursor.execute("DELETE FROM consultorio where codigo='"+codigo+"'")
			print("Consultorio eliminado exitosamente")
		except:
			print("Error al elimiar dato")
	elif op == 2:
		print("Has cancelado la eliminacion del consultorio")
	else:
		print("Opcion no valida, los datos no se has eliminado")

	con.commit()
	cursor.close()
	con.close()


menu()