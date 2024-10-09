"""
CADENAS DE CARACTERES
"""

s1 = "Hola"
s2 = "Sergio"

#Concatenación
print(s1 + " " + s2  + "!")

#Repetición
print(s1 * 3)

#Indexación
print(s1[0] +s1[1] + s1[3])

#Longitud
print(len(s2))

#Slicing (porción)
print(s2[2:6]) #inicia en la posición 2 y acaba en la 5
print(s2[2:]) #si no se pone nada llega hasta el final

#Búsqueda
print("Ho" in s1)
print("i" in s1)

#Reemplazo
print(s1.replace("o", "a"))

#División
print(s2.split("r"))

#Conversión a mayúsculas y minúsculas
print(s1.upper())
print(s2.lower())
print("kas borrella".title()) #inicia cada palabra en mayúscula
print("kas borrella".capitalize()) #solo pone la primera

#Eliminación de espacios al principio y al final
print(" kas borrella ".strip() + "QA") 

#Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("la"))
print(s1.endswith("Ho"))
print(s1.endswith("la"))

#Búsqueda de posición
print("Kas Borrella QA".find("QA"))
print("Kas Borrella QA".lower().find("b")) #convierte todo en minúscula y busca la b 

s3 = "Kas Borrella QA"
#Busqueda de ocurrencias
print(s3.lower().count("a"))

#Formateo
print("Saludo: {} nombre: {} !".format(s1, s2))

#Interpolación
print(f"Saludo: {s1} nombre: {s2} !") #la "f" del principio hace referencia a cualquier variable que hayas definido

#Transformación en lista de caracteres
print(list(s3))

#Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]

print("".join(l1))

#Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)
s5 = "1234.56"
s5 = float(s5)
print(s5)

#Comprobaciones varias
s4 = "1234567"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
EXTRA
"""
def check(word1: str, word2: str):
    
    #Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")


    #Anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    #Isograma
    print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")

    def isogram(word: str) -> bool:

        word_dict = dict()
        for word in word:
            word_dict[word] = word_dict.get(word, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
        
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")

check("radar", "kas")
check("amor" , "roma")


