#ejercicio 1          bucle for para iterar elementos en estructuras de datos (listas, tuplas, etc).
fruits = {"banana", "apple", "kiwi"}
for x in fruits:
    print(x)
# banana
# apple
# kiwi

# ejercicio 2  bucle con string.
y = "hello"
for x in y:
    print(x)
# h
# e
# l
# l
# o
     
#ejercicio 3     break para salir del bucle cuando x == l.
y = "hello"
for x in y:
    if x == "l":
        break
    print(x)
# h
# e
    
#ejercicio 4    usando continue se salta el ciclo donde se imprimiria kiwi y apsa al siguiente.

fruits = {"banana", "apple", "kiwi", "watermelon"}
for x in fruits:
    if x == "kiwi":
        continue
    print(x)
# apple
# watermelon
# banana
    
#ejercicio 5  si se quiere ejecutar cierto numero de veces un conjunto de codigo se puede usar funcion range().

lista = []
for x in range(5):
    lista.append(x)
    print(lista)
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
    
#ejercicio 6           de 0 a 10 de 2 en 2.
for x in range(0,10,2):
    print(x)
# 0
# 2
# 4
# 6
# 8
    
#ejercicio 7     se puede usar else cuando se termine el bucle. 
                 #Nota el else no se ejecuta si se ejecuta antes un break.
i = 0
for x in range(4):
    i += 1
    print(i)
else:
    print("Se acabo el bucle.")
# 1
# 2
# 3
# 4
# Se acabo el bucle.
    
#ejercicio 8  en este caso se ejecuta el break en x == 3 y no se ejecuta el else. Pasa igual en el while.
i = 0
for x in range(4):
    if x == 3: break
    i += 1
    print(i)
else:
    print("Se acabo el bucle.")
# 1
# 2
# 3
    
#ejercicio 9       for anidados.
adjunto = ["red", "big", "tasty"]
fruits = ["banana", "apple", "kiwi", "watermelon"] #para cada x en adjunto, imprima x y cada Y en frutas.

for x in adjunto:
    for y in fruits:
        print(x,y)
# red banana
# red apple
# red kiwi
# red watermelon
# big banana
# big apple
# big kiwi
# big watermelon
# tasty banana
# tasty apple
# tasty kiwi
# tasty watermelon

#ejercicio 10     #por si necesitaramos y ciclo for sin contenido usamos pass.
for x in [0, 1, 2]:
  pass