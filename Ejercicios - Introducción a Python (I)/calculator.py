#calculator.py
#Crear las sentencias necesarias para recoger dos números a través del terminal
#Integrar funcionalidades de suma, resta, multiplicación, división, y exponencial
#Implementar funciones, diccionarios, y excepciones
#Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)
#Realizar las operaciones e imprimir el valor por pantalla.
#Subir el archivo a vuestra cuenta de GitHub 

def sumar(numero_a, numero_b):
    return numero_a + numero_b

def restar(numero_a, numero_b):
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b

def dividir(numero_a, numero_b):
    return numero_a / numero_b

def exponenciar(numero_a, numero_b):
    return numero_a ** numero_b


def configuracionInicial():
    print("Lista de opciones permitidas")
    print("\t 0 = 'SUMAR'")
    print("\t 1 = 'RESTAR'")
    print("\t 2 = 'MULTIPLICACION'")
    print("\t 3 = 'DIVISION'")
    print("\t 4 = 'EXPONENCIAR'")

def isOpcionValida(opcion):
    opcionValida = False
    if opcion < 5 and opcion >= 0:
        opcionValida = True
    return opcionValida

def realizarOperacion(opcion, numero_a, numero_b):
    resultado = {
        'SUMAR': sumar(numero_a, numero_b),
        'RESTAR': restar(numero_a, numero_b),
        'MULTIPLICACION': multiplicar(numero_a, numero_b),
        'DIVISION': dividir(numero_a, numero_b),
        'EXPONENCIAR': exponenciar(numero_a, numero_b)
    }
    return resultado[opcion]

if __name__ == "__main__":
    try:
        #Aqui empezamos el programa
        continuar = True
        opciones = {
            0: 'SUMAR',
            1: 'RESTAR',
            2: 'MULTIPLICACION',
            3: 'DIVISION',
            4: 'EXPONENCIAR'
        }
        while continuar:
            configuracionInicial()
            opcion_escogida = int(input("Eliga la opción (en numero): "))
            if isOpcionValida(opcion_escogida):
                opcion = opciones[opcion_escogida]
                numero_a = float(input("Introduzca el primer numero: "))
                numero_b = float(input("Introduzca el segundo numero: "))
                resultado = realizarOperacion(opcion, numero_a, numero_b)
                print(f"El resultado de la operación {opcion} ha sido de: {resultado}")
            else:
                print("Opcion no válida, vuelva a intentarlo")
            desea_continuar = int(input("¿Desea continuar? 0: NO: "))
            if desea_continuar == 0:
                continuar = False
    except Exception as error:
        print("Ha ocurrido un error en el main...")
        print(f"{error}")

            