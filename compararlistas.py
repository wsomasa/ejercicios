"""desarrollar un programa que permita conocer, si el primer y ultimo elemento de una lista son el mismo número"""
mensaje= "Quieres conocer si el primer y ultimo numero de la lista son iguales"
print('\n\t''\n\t''\033[93m', mensaje.center(80, "*"),'\033[0m')
nombre = input('\n\t'"Ingresa tu nombre: ")
print('\n\t'"Hola", nombre, "ingresa cinco números en la lista, para comparar si el primero y el ultimo son iguales"'\n')

lista = []

for i in range(5):
    numero = int(input('\n\t'"Ingresa un numero: "))
    lista.append(numero)

if lista[0] == lista[-1]:
    print('\n\t''\033[92m'"El primer número y el ultimo numero son iguales"'\n''\033[0m')
else: 
    print('\n\t''\033[91m'"Lo siento ", nombre, "los números no son iguales"'\n''\033[0m')

