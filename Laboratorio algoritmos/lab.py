#Elaborar un programa que tenga un archivo de texto
#llamado EN-ES.txt el cual contiene las traducciones de palabras
#del ingles al español

def cargar_diccionario(archivo):
    diccionario = {}
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                clave, valor = linea.strip().split('=')
                diccionario[clave] = valor
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    return diccionario

def agregar_traduccion(archivo, palabra_ingles, palabra_espanol):
    try:
        with open(archivo, 'a') as file:
            file.write(f"\n{palabra_ingles}={palabra_espanol}")
        print(f"Traducción agregada: {palabra_ingles} -> {palabra_espanol}")
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")

def traducir(diccionario, idioma, palabra):
    if idioma == 'EN-ES':
        if palabra in diccionario:
            return diccionario[palabra]
        else:
            return "Palabra no encontrada en el diccionario."
    elif idioma == 'ES-EN':
        palabras = [key for key, value in diccionario.items() if value == palabra]
        if palabras:
            return ", ".join(palabras)
        else:
            return "Palabra no encontrada en el diccionario."
    else:
        return "Idioma no válido. Use 'EN-ES' o 'ES-EN'."

if __name__ == "_main_":
    archivo = "EN-ES.txt"
    diccionario = cargar_diccionario(archivo)
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar nueva traducción")
        print("2. Traducir")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            palabra_ingles = input("Ingrese la palabra en inglés: ")
            palabra_espanol = input("Ingrese la traducción en español: ")
            agregar_traduccion(archivo, palabra_ingles, palabra_espanol)
        elif opcion == "2":
            idioma = input("Seleccione el idioma (EN-ES o ES-EN): ")
            palabra = input("Ingrese la palabra a traducir: ")
            resultado = traducir(diccionario, idioma, palabra)
            print(f"{idioma} {palabra} --> {resultado}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
