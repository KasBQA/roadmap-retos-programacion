"""
ESCTRUCTURAS DE DATOS
"""

#Listas

list = ["Kas", "Sergio", "Eric", "Alex"]
print(list)
list.append("Alma") #append añade al final un nombre a la lista/array
print(list)
list.remove("Kas") #elimina datos
print(list)
print(list[2]) #accede al nombre que haya en la posición 2
list[2] = "Alma" #actualización
print(list)
list.sort() #Ordenación, lo hace por orden alfabetico por defecto
print(list)


#Tuplas (estructura que guardas más de un dato, son inmutables)

my_tuple = ("Kas", "B", "36")
print(tuple[0]) #Acceso
my_tuple = tuple(sorted(my_tuple))
print(type(my_tuple))

#Sets
my_set = {"Kas", "B", "36"} #son estructuras que sirven para guardar muchos datos, pero no los ordena, en algunos lenguajes se encuentra como Hash Set
print(my_set)
my_set.add("kasb@gmail.com") #Insercción
my_set.add("kasb@gmail.com") #no se añade 2 veces, a cada dato le da una clave alfanúmerica (un hash) 
print(my_set)
my_set.remove("Kas") #Eliminación
print(my_set)
#No se puede ordenar por definición

# Diccionario
my_dict: dict = {
    "name":"Kas",
    "surname":"B",
    "age": "34"
} #aunque vaya con corchetes, se diferencia del set porque se le da una clave {"clave": "x"}
print(my_dict)
print(my_dict["name"]) #Acceso
my_dict["email"] = "kasb@gmail.com" #Insercción
print(my_dict)
my_dict["age"] = "35" #Actualización
print(my_dict)
del my_dict["surname"] #Eliminación
print(my_dict)

print(type(my_dict))

"""
Extra
"""
#AGENDA DE CONTACTOS

def my_agenda():

    agenda = {}

    #creamos una función que se va a usar en más de un caso, para no repetir código
    def insert_contact():
        phone = input("Introduce el número de teléfono: ")
        if phone.isdigit() and len(phone) >0 and len(phone) <= 11: #isdigit comprueba que sean digitos y len la longitud
            agenda[name] = phone
        else:
            print("Debes introducir un número entre 1 y 11 dígitos")      
    


    while True: #Espera que una condición sea verdadera

        print("")
        print("1.Buscar contacto")
        print("2.Insertar contacto")
        print("3.Actualizar contacto")
        print("4.Eliminar contacto")
        print("5.Mostrar todos los contactos")
        print("6.Salir")

        option = input("\nSelecciona una opción:")

        match option: #match es el case de java           
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}")

                else:
                    print(f"El contacto no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()                   
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                   insert_contact()                  
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto no existe.")
            case "5":
                if agenda:
                    print("Contactos guardados:")
                    for name, phone in agenda.items():
                        print(f"Nombre: {name}, Teléfono: {phone}")
                else:
                    print("No hay contactos en la agenda.")
            case "6":
                print("Saliendo de la agenda")
                break #cuando se ejecute esta linea se sale del bucle
            case _: 
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()