# #02 FUNCIONES Y ALCANCE

"""
Funciones definidas por el usuario
"""

#Simples

def greet():
    print("Hola, Python!")

greet()

#Con retorno

def return_greet():
    return "Hola, Pyton"

greet = return_greet()
print(return_greet())

#Con argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Kas")

#Con un argumento predeterminado

def default_arg_greet(name="Python"): #Valor por defecto
    print(f"Hola, {name}")

default_arg_greet("Kas")
default_arg_greet() #si se deja vacío el () llamará al nombre por defecto

#Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hola", "Kas"))


#Con retorno de varios valores

def multiple_return_greet():
    return "Hola","Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

#Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola,{name}")

variable_arg_greet("Pyton", "Kas", "Comunidad")

#Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola,{value}({key})")

variable_key_arg_greet(
    language="Python",
    name="Kas",
    people="Comunidad",
    edad="34"
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcioón interna:Hola Kas")
    inner_function()

outer_function()

"""
Funciones de lenguaje (built-in)
"""
print(len("KasQa")) #len cuenta la cantidad de caracteres de una linea de texto
print(type("KasQa")) #tipo de dato que le pasamos a la cadena de texto, en este caso un string
print("kas".upper()) #convierte la palabra en mayuscula

"""
Variables locales y globales
"""

global_variable = "Eric"

print(global_variable)

def hello_kid():
    local_var = "Hola" #no se va poder imprimir fuera de esta función
    print(f"{local_var}, {global_variable}") #imprime una variable que está fuera de la propia función, es decir, una variable que vale para todas las funciones

hello_kid()


"""
Extra 
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)        
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz","Buzz"))