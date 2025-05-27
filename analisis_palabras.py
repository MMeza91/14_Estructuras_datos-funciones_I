f= open("./lorem_ipsum.txt", "r") 
texto = f.read()

palabras=texto.split()
print(palabras)

palabra_borrada=[]
words=[]
for i in palabras:
    words.append(i)
    contador=0
    for e in words:
        if i==e:
            contador+=1
        
    if contador>1:
        borrada=words.pop()
        palabra_borrada.append(borrada)
        
print("\n\n")
print(palabra_borrada)
print("_"*100)
print("\n\n")
print(words)
print(len(words))
    
