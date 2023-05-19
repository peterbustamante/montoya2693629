diccionario_español_ingles = {}
diccionario_ingles_español = {}

def agregar_animal():
    nombre_español = input("Ingrese el nombre del animal en español: ")
    nombre_ingles = input("Ingrese el nombre del animal en inglés: ")

    diccionario_español_ingles[nombre_español] = nombre_ingles
    diccionario_ingles_español[nombre_ingles] = nombre_español

def traducir_español_ingles():
    palabra = input("Ingrese una palabra en español: ")
    if palabra in diccionario_español_ingles:
        traduccion = diccionario_español_ingles[palabra]
        print(f"Traducción al inglés: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def traducir_ingles_español():
    palabra = input("Ingrese una palabra en inglés: ")
    if palabra in diccionario_ingles_español:
        traduccion = diccionario_ingles_español[palabra]
        print(f"Traducción al español: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def mostrar_menu():
    while True:
        print("Menu")
        print("1. Agregar animal")
        print("2. Traducir del español al inglés")
        print("3. Traducir del inglés al español")
        print("4. Salir")



