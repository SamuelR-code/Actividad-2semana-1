#Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista usando in.

lista = [2,4,8,7,3 ]

numero_usu=int(input("Ingrese un numero"))

if numero_usu in lista:
    print("Esta en la lista")
else:
    print("No esta en la lista")

