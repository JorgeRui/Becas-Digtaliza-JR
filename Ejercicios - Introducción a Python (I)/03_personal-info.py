#Script para preguntar el nombre, tlf y ciudad
nombre = input("¿Cúal es su nombre?: ")
tlf = int(input("¿Cúal es su teléfono?: "))
ciudad = input("¿Cúal es su ciudad?: ")
edad = int(input("¿Cúal es su edad?: "))

print("Bienvenido {}, usted reside en {}, su teléfono particular es {} y su edad actual es {} años"
.format(nombre, ciudad, tlf, edad))