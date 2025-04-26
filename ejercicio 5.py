#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

nombres=["Ana","Luis","Sofia"]
nombre_usu=input("ingrese su nombre")

if nombre_usu in nombres:
  print("Estas en la lista")

else:
  print("No estas en la lista")