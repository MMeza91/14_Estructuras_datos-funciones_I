import sys

# Las distintas tasas de conversión se deben ingresar en el siguiente orden: Sol, Peso Argentino, Dólar Estadounidense.
incorrecto=True
while incorrecto:
    try: 
        if len(sys.argv) > 1:
            tasa_sol= float(sys.argv[1])
            tasa_argento= float(sys.argv[2])
            tasa_gringo= float(sys.argv[3])
            monto= float(sys.argv[4])
        else:
            tasa_sol= float(input("ingrese la tasa de conversión de Peso Chileno a Sol Peruano: "))
            tasa_argento= float(input("ingrese la tasa de conversión de Peso Chileno a Peso Argentino: "))
            tasa_gringo= float(input("ingrese la tasa de conversión de Peso Chileno a Dolar Estadounidense: ")) #América es un continente no un país
            monto= float(input("ingrese el monto a evaluar en Pesos Chilenos: "))
        incorrecto=False
    except:
        print("\nAlgunos de los VALORES son INCORRECTOS\n\n")
        sys.argv=[]

conv_sol=monto*tasa_sol
conv_argento=monto*tasa_argento
conv_gringo=monto*tasa_gringo

print(f"\nLos {monto:.1f} Pesos Chilenos equivalen a:")
print(f"{conv_sol:.1f} Soles Peruanos")
print(f"{conv_argento:.1f} Pesos Argentinos")
print(f"{conv_gringo:.1f} Dólares Estadounidenses\n")