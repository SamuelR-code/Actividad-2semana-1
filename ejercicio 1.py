#Pide tres números al usuario.
#Usa condicionales (if) para decir cuál es el más pequeño.
numero1=int(input("ingrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))
numero3=int(input("ingrese el tercer numero"))

if numero1<=numero2 and numero1<=numero3:
    print("El primer numero es el mas pequeño")
elif numero2<=numero1 and numero2<=numero3:
    print("El segundo numero es el mas pequeño")
else:
    print("El tercer numero es el mas pequeño")