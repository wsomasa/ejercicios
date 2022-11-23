nombre = "Walter"
apellido = "Somasa"
segundo_apellido = "Amaya"

#LAS CONSTANTES SE DECLARAN EN MAYUSCULAS
PI = 3.1416
print(PI)
print(nombre)
print(apellido)
print(PI)
PI = 3.12
print(PI)

suma = 2 + 2
print(suma)

valor = 3 > 5
print(valor)

if nombre == "Walter":
    print(nombre)
else:
    print("Tu no eres Walter")
    
edad = 55

if edad == 18:
    print("Eres mayor de edad")
elif edad == 15:
    print("casi eres mayor de edad")
elif edad == 1:
    print("Eres un pequeño")
elif edad >= 50:
    print("Eres mayorcito para jugar con computadoras")
else:
    print("Eres menor de edad")
    
edad = int(input("Ingrese su edad: "))
if edad == 55 and nombre == "Walter":
    print(nombre, "Es adulto")
else:
    print("Eres joven todavia")