import csv
from datetime import datetime

with open('datos.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    lista = list(reader)[0]

login = input("Introduzca su usuario ")
while login not in lista:
    print("Acceso Denegado")
    login = input("Introduzca su usuario: ")

print("Acceso Concedido")

#Agregar nuevo usuario
lista.append("")

# Reemplazar los valores de la lista con asteriscos
lista = ['*' * len(usuario) for usuario in lista]


#Escribir la lista actualizada en el archivo CSV

with open("datos.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(lista)


with open("Hora.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([login, datetime.now()])


