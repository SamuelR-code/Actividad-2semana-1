#Pide al usuario su edad.
#Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

edad_usu=int(input("Ingrese su edad"))

if edad_usu<0 and edad_usu>120:
    print("edad no valida")
else:
    print("Edad valida")
