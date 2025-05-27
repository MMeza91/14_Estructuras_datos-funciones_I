import sys

programa=True
#while programa:
#    inicio=True
#    while inicio:
if len(sys.argv) >1:
    archivo = str(sys.argv[1])
    print(archivo)
else:
    archivo = str(input("Escribe el nombre del archivo (que se encuentre en la misma carpeta): "))
    
with open(archivo, "r", encoding="utf-8") as f:
    texto = f.read()
inicio=False

print("El el archivo no existe o está en otra carpeta\n")
sys.argv = []
inicio=True



palabras=archivo.split()

palabras_distintas = set(palabras)
letras_distintas = set(archivo)