#ejercicio 1
lista = ["apple", "banana", "cherry"]  #las listas se crean usando [].
print(list)
#los elementos de una lista SON ordenados(orden de los elementos segun se ingresan), modificables, y permite duplicar valores.
#cada posicion esta representada por un indice, desde 0.
#al ser ordenada si añadimos un nuevo item este se añadira el final.

#ejercicio 2
names = ["Juan", "Sebastian", "Luisa", "Juan"] #permite duplicados.

#ejercicio 3
names = ["Juan", "Sebastian", "Luisa", "Juan"]
print(len(names))           #metodo len() para saber el numero de elementos de la lista.
# 4

#ejercicio 4
names = ["Juan", "Sebastian", "Luisa", "Juan"]
numbers = [1, 2 ,3 ,4]                          #una lista puede ser de cualquier tipo de dato.
lista = [True, False, False]

#ejercicio 5
variado = ["Juan", 1, 2.5, False]  #las listas pueden contener diferentes tipos de datos.

#ejercicio 6
lista = ["Juan", 1, 2.5, False]  #es definido como tipo dato list.
print(type(lista))
# <class 'list'>

#ejercicio 6
animales = list(["perro", "gato","pajaro"]) #tambien se puede utilizar un constructor para crear una lista.

#ejercicio 7
fruits = ["banana", "apple", "orange", "banana"]
print(fruits[1])                                       #acceder y muestra el segundo item de la lista.
# apple

#ejercicio 8
fruits = ["banana", "apple", "orange", "banana"]       #si se usa el negativo comienza de derecha a izquierda desde -1.
print(fruits[-1])
# banana

#ejercicio 9
fruits = ["banana", "apple", "orange", "banana"] 
print(fruits[-4:3])                                   #para seleccionar ciertos elementos en especificos sin tomar el ultimo.
#['banana', 'apple']

#ejercicio 10
fruits = ["banana", "apple", "orange", "banana"] 
print(fruits[:2])
#['banana', 'apple']

#ejercicio 11
fruits = ["banana", "apple", "orange", "banana"] 
print(fruits[2:])
#['orange', 'banana']

#ejercicio 12
fruits = ["banana", "apple", "orange", "banana"] #de derecha a izquierda desde el 1. 
print(fruits[-3:-1])
#['apple', 'orange']

#ejercicio 13
fruits = ["banana", "apple", "orange", "banana"]
print("apple" in fruits)
#True
print("kiwi" in fruits)
#False

#ejercicio 14
fruits = ["banana", "apple", "orange", "banana"]    #modificar un elemento de la lista.
fruits[1] = "cherry"
#['banana', 'cherry', 'orange', 'banana']

#ejercicio 15
fruits[0:2] = ["watermelon", "kiwi"]  #siguiendo la misma dinamica desde 0 hasta 2 sin coger el 2, pero para modificar.
#['watermelon', 'kiwi', 'orange', 'banana']

#ejercicio 16
fruits = ["banana", "apple", "orange", "banana"] #si se insertan mas datos de los seleccionados este se agrega y corre rl resto.
fruits[0:1] = ["watermelon", "kiwi"]
#['watermelon', 'kiwi', 'apple', 'orange', 'banana']

#ejercicio 17
fruits = ["banana", "apple", "orange", "banana"]
fruits[0 : 2] = ["kiwi"]    #por otro lado si se insertan menos solo quedara el nuevo insertado. Ojo con los corchetes.
#['kiwi', 'orange', 'banana']

#ejercicio 18
fruits = ["banana", "apple", "orange", "banana"] #metodo insert, desplaza el que esta en la posicion a rigth y pone el nuevo.
fruits.insert(2,"watermelon")
#['banana', 'apple', 'watermelon', 'orange', 'banana']

#ejercicio 19
cars = ["nissam", "ford", "ferrari"]    #metodo append() para agregar un elemento al final de la lista.
cars.append("bmw")
#['nissam', 'ford', 'ferrari', 'bmw'].

#ejercicio 20
cars = ["nissam", "ford", "ferrari"]
fruits = ["banana", "apple", "orange", "banana"]    #metodo extend() para adjuntar elementos de otra lista.
cars.extend(fruits)
#['nissam', 'ford', 'ferrari', 'banana', 'apple', 'orange', 'banana'].

#ejercicio 21
cars = ["nissam", "ford", "ferrari"]
sports = ("swimming", "soccer", "basketball")   #puede ser entre diferentes tipos, em este caso se extendio con una tupla.
cars.extend(sports)                             #puede ser con diccionarios, tuplas, conjuntos, etc.
#['nissam', 'ford', 'ferrari', 'swimming', 'soccer', 'basketball']

#ejercicio 22
sports = ["swimming", "soccer", "basketball"]   #metodo remove() para quitar algun elemento.
sports.remove("soccer")                         #si hay varios elemntos iguales se remueve desde izquierda el primero.
#['swimming', 'basketball']

#ejercicio 23
sports = ["swimming", "soccer", "basketball"]   #metodo pop() para remover cierto index(indice).
sports.pop(0)                                   #si no se especifica remueve el ultimo elemento.
#['soccer', 'basketball']

#ejrcicio 24
sports = ["swimming", "soccer", "basketball"]   #parabra clave del para eliminar un index,
del sports[1]   
#['swimming', 'basketball']

#ejercicio 25
sports = ["swimming", "soccer", "basketball"]   #elimina la lista completa
del sports  

#ejercicio 26
sports = ["swimming", "soccer", "basketball"]   #limpia la lista.
sports.clear()

#ejercicio 27
sports = ["swimming", "soccer", "basketball"] 
deportes = []
for x in sports:
    print(x)
    deportes.append(x)

#al imprimir la lista --> deportes = ['swimming', 'soccer', 'basketball'].

#ejercicio 28
sports = ["swimming", "soccer", "basketball"] #formas para recorrer una lista con bucles.
for x in sports:
    print(x)
#swimming
#soccer
#basketball
    
#ejercicio 29 
sports = ["swimming", "soccer", "basketball"] 
for x in range(len(sports)):
    print(sports[x])
    print(x)
#swimming
#soccer
#basketball
    
#ejercicio 30
i = 0
sports = ["swimming", "soccer", "basketball"] #recorrer una lista con el bucle while.
while i < len(sports):
    print(sports[i])
    i += 1              #se incrementa en 1 la variable 1
#swimming
#soccer
#basketball
    
#----------------------------    

#ejercicio 31
sports = ["swimming", "soccer", "basketball"] #usos de list comprehension.
new = [x for x in sports if "i" in x]         #nueva lista = [de que se llenara la lista "con variable" - for - variable - in "lista" condicion].
# new contendria ['swimming']

#ejercicio 32 "crear una lista con el doble de los elementos de 'numeros'"
numeros = [1, 2, 3, 4, 5]
doble = [x * 2 for x in numeros]              #en este caso se debe crear una nueva lista que contenga del doble de la de numeros.
print(doble)                                  #no fue necesario usar una condicion.
#[2, 4, 6, 8, 10]

potencia = [x ** 2 for x in numeros] 
print(potencia)
#[1, 4, 9, 16, 25]

#ejercicio 33 "crear una lista con los elementos de 'palabras' que sobrepasen las 3 letras"
palabras = ["sol", "luna", "estrella", "cielo", "nube"] #en este no se le da cambio a los elementos pero si se implementa una condicion
largas = [x for x in palabras if len(x) > 3]
print(largas)
#['luna', 'estrella', 'cielo', 'nube']

#ejercicio 34 "crear una nueva lista que contenga la longitud de cada palabra mayor a 3 caracteres"
palabras = ["python", "es", "muy", "poderoso", "y", "versátil"]
longitud = [len(x) for x in palabras if len(x) > 3]
#[6, 8, 8]

#ejercicio 35 "Only accept items that are not "apple" "
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
lista_nueva = [x for x in fruits if x != "apple"]
#['banana', 'cherry', 'kiwi', 'mango']

#ejercicio 36
lista_range = [x for x in range(10)] #con funcion range() como el iterable.
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#ejercicio 37
lista_condicional = [x for x in range(5, 11) if x % 2 == 0] #solo numeros pares desde el 5 hasta el 10.
#[6, 8, 10]

#ejercicio 38
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  #ejem poner el resultado en mayusculas.
nueva_lista = [x.upper() for x in fruits]
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruit_m = ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
new_list = [x.lower() for x in fruit_m]
#['apple', 'banana', 'cherry', 'kiwi', 'mango']

#ejercicio 39
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  #poner el resultado como quiera.
new = ["hello" for x in fruits]
#['hello', 'hello', 'hello', 'hello', 'hello']

#ejercicio 40
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  #con operador ternario.
new = [x if x == "banana" else "orange" for x in fruits] #devuelva x si x es == "banana", sino devuelva "orange"
#['orange', 'banana', 'orange', 'orange', 'orange']

#----------------------------

#ejercicio 41 
fruits = [ "banana", "kiwi", "cherry", "mango", "apple", ["watermelon", "orange"]] #metodo para ordenar ascendentemente.
print(fruits[5][1][4])
# g

fruits = [ "banana", "kiwi", "cherry", "mango", "apple"]
fruits.sort()


#['apple', 'banana', 'cherry', 'kiwi', 'mango']

#ejercicio 42
numbers = [100, 50, 65, 82, 23]
numbers.sort()
#[23, 50, 65, 82, 100]

#ejercicio 43
numbers = [23, 50, 65, 82, 100]  #se le añade la palabra clave reverse como argumento para hacerlo decreciente.
numbers.sort(reverse=True)
#[100, 82, 65, 50, 23]

#ejercicio 44
fruits = [ "banana", "kiwi", "cherry", "mango", "apple"] #metodo de reversa.
fruits.reverse()
#['apple', 'mango', 'cherry', 'kiwi', 'banana']

#----------------------------

#ejercicio 45
#copiar una lista lista1 = lista2 
#forma correcta con metodo copy(), o con metodo list()

fruits = ["kiwi", "cherry", "mango", "apple"]
new_list = fruits.copy()
#['banana', 'kiwi', 'cherry', 'mango', 'apple']

lista = fruits

fruits = [ "banana", "kiwi", "cherry", "mango", "apple"]
new = list(fruits)
#['banana', 'kiwi', 'cherry', 'mango', 'apple']

#----------------------------

#ejercicio 46
lista_uno = ["a", "b", "c"]     #unir dos listas
lista_dos = [1, 2, 3]
lista_union = lista_uno + lista_dos
#['a', 'b', 'c', 1, 2, 3]

#ejercicio 47
lista_uno = ["a", "b", "c"]     #con for
lista_dos = [1, 2, 3]
for x in lista_dos:
    lista_uno.append(x)
#lista_uno = ['a', 'b', 'c', 1, 2, 3]

#ejercicio 48
lista_uno = ["a", "b", "c"]     #con metodo extend
lista_dos = [1, 2, 3]
lista_uno.extend(lista_dos)
#lista_uno = ['a', 'b', 'c', 1, 2, 3]

#ejercicio 49
lista = [['watermelon', 'kiwi'], 'apple', 'orange', 'banana']
print(lista[0][1])
#kiwi

#ejercicio se tamaño
import sys

lista = [1, 2, 3]
tupla = (1, 2, 3)

# Tamaño en memoria de la lista
tamano_lista = sys.getsizeof(lista)

# Tamaño en memoria de la tupla
tamano_tupla = sys.getsizeof(tupla)

print("Tamaño en memoria de la lista:", tamano_lista, "bytes")
# Tamaño en memoria de la lista: 88 bytes
print("Tamaño en memoria de la tupla:", tamano_tupla, "bytes")
# Tamaño en memoria de la tupla: 64 bytes



#----------------------------

#LISTADO DE METODOS DE LISTAS
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
