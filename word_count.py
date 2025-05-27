import sys

programa=True
while programa:
    inicio=True
    while inicio:
        try:
            if len(sys.argv) >1:
                archivo = str(sys.argv[1])
                print("\nBienvenida/o a este programa para analizar documentos:")

            else:
                archivo = str(input("\nEscribe el nombre del archivo (que se encuentre en la misma carpeta): "))

            f= open(archivo, "r") 
            texto = f.read()
            inicio=False
            print("Estamos analizando el archivo que nos entregaste...\n")

        except FileNotFoundError:
            print("El el archivo no existe, está mal escrito (puede que le falte la extensión) o está en otra carpeta. \n\n¡Prueba de nuevo!\n")
            sys.argv = []
            inicio=True



    palabras=texto.split()


    palabras_distintas = set(palabras)
    print(f"El número de parabras distintas es: {len(palabras_distintas)}")
    letras_distintas = set(texto)
    print(f"El número de letras distintas es: {len(letras_distintas)}")

    pregunta=True
    while pregunta:
        respuesta=input("\nDesea analizar otro texto? (Si/No): ")
        if respuesta.lower()=="si" or respuesta.lower()=="s":
            sys.argv = []
            print("Genial, intentemos con otra")
        elif respuesta.lower()=="no" or respuesta.lower()=="n":
            programa=False
            print("Nos vemos en una próxima\n")
        else: 
            print("El valor ingresado no es valido, responda si o no\n")
        pregunta=False