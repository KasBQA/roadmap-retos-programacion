"""
01 OPERADORES Y ESTRUCTURAS DE CONTROL
"""
#Operadores Arigméticos
print("Operadores Arigméticos:")
sum = {10 +3} #se puede meter en una variable
print(f"Suma: 10 + 3 = {10 + 3}") #solo lo de dentro de las llaves es código, lo otro es texto (string)
print(f"Suma: 10 +3 = {sum}") #la variable la puedes indicar y te hace la suma indicada
print(sum) #o pintar solo la variable
print(f"Resta: 10 - 3 = {10 -3 }")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

#Operadores de comparación
print("Operadores de comparación:")
print(f"Igualdad: 10 == 3 es {10 == 3}") #no solo se usan con números, tambien con variables y demás
print(f"Desigualdad 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

#Operadores lógicos
print("Operadores lógicos:")
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") #exige que las 2 condiciones sean verdaderas
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 5 es {10 + 3 == 13 or 5 - 1 == 5}") #solo pide que una de las dos condiciones sean veraderas
print(f"OR ||: 10 + 3 == 16 or 5 - 1 == 5 es {10 + 3 == 16 or 5 - 1 == 5}") #aquí dará resultado False porque no se cumple ninguna
print(f"NOT !: 10 + 3 == 14 es {not 10 + 3 == 14}")

#Operadores de asignación
print("Operadores de asignación:")
my_number = 11 #el igual sirve para asignar el valor 11 a la variable my_number
print(my_number)
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 
print(my_number)
my_number *= 2 
print(my_number)
my_number /= 2 
print(my_number)
my_number %= 2
print(my_number)
my_number **= 2
print(my_number)
my_number //= 2
print(my_number) 

#Operadores de identidad
print("Operadores de identidad:")
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}") #usa posiciones de memoria, no de valor
print(f"my_number is not my_new_number es {my_number is not my_new_number}") 

# Operadores de pertenencia
print("Operadores de pertenencia")
print(f"'a' in 'Kas' = {'a' in 'Kas'}")
print(f"'b' not in 'Kas' = {'b' not in 'Kas'}")

#Operadores de bit
print("Operadores de bit")
a = 10 # 1010
b = 3 # 0011
print(f"AND : 10 & 3 = {10 & 3}") #0010
print(f"OR : 10 | 3 = {10 | 3}") #1011
print(f"XOR : 10 ^ 3 = {10 ^ 3}") #1001
print(f"NOT : ~10  3 = {~10}") #1001
print(f"Desplazamiento a la derecha: 10 >> 2 =  {10 >> 2}") #0010
print(f"Desplazamiento a la derecha: 10 << 2 =  {10 << 2}") #10100

"""
Estructura de control
"""

#Condicionales
my_string = "KasQa"

if my_string == "KasQa":
    print("my_string es 'KasQa'")
elif my_string == "KasB":
    print("my_string es 'KasB'")
else:
    print("my_string no es ''KasQa' ni 'KasB'")


#Iterativas
#nos valen para recorrer estructuras con mas de un elemento o ejecutar una accion varias veces
for i in range(11):
    print(i)

#se ejecuta mientras la condicion sea verdadera
i = 0
while i <= 10:
    print(i)
    i +=1 #como sumas 1 a 0 que es la variable 'i', cuando llegue a 10 para

#Manejo de excepciones
try:
    print(10 / 0)
except: #es el equivalente al "catch en java"
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


"""
Extra
"""

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)