numero = int(input("Introduzca un numero: "))
numero = abs(numero)
if numero < 20:
    print("El numero introducido es: {}".format(numero))
elif numero >= 20 and numero <=39:
    print("El numero introducido es: {}".format(numero))
elif numero > 39 and numero <= 59:
    print("El numero introducido es: {}".format(numero))
elif numero > 59:
    print("El numero introducido es: {}".format(numero))
