#ejercicio 1
thistuple = ("apple", "banana", "cherry") #forma de crear una tupla.

#ejercicio 2
fruits = ("orange", "orange", "banana") #permite valores repetidos. 

#ejercicio 3
fruits = ("orange", "orange", "banana")
len(fruits) #funcion len() para saber el numero de elemntos de la tupla.
# devuelve 3

#ejercicio 4 
fruits = ("orange",) #para poder declarar una tupla de solo un elemento hay que poner una coma, de lo contrario contara como un string.
type(fruits)
# <class 'tuple'>               

fruits = ("orange") 
type(fruits)
# <class 'str'>

#ejercicio 5
string_tuple = ("orange", "orange", "banana")
number_tuple = (1, 2, 3, 4)
boolean_tuple = (True, False, False)

#ejercicio 6
tupla = ("orange", 1, 1.5, True) #la tupla puede contener varios tipos de datos a la vez.

#ejercicio 7
fruits = ("orange", "orange", "banana") #funcion type() con tupla.
type(fruits)
# <class 'tuple'>

#ejercicio 8
fruits = tuple(("orange", "orange", "banana")) #crear tupla con el constructor tuple().

#----------------------------

#ejercicio 9
fruits = ("orange", "orange", "banana") #para acceder al index de la tupla se hace con corchetes, como en la lista.
fruits[0]
# 'orange'

#ejercicio 10
fruits = ("orange", "orange", "banana") #igual con los negativos de derecha a izquiera desde -1
fruits[-1] #'banana'
fruits[-2] #'orange'

#ejercicio 11
fruits = ("orange", "orange", "banana", "kiwi", "apple") #igual con rangos. Desde 0 (lo agrega) hasta el 2 (no lo agrega).
fruits[0:2] #('orange', 'orange')

#ejercicio 12
fruits = ("orange", "orange", "banana", "kiwi", "apple") #igualdesde el inicio.
fruits[:3] #('orange', 'orange', 'banana')

#ejercicio 13
fruits = ("orange", "orange", "banana", "kiwi", "apple") #igual desde cierto indice hasta el final.
fruits[2:] #('banana', 'kiwi', 'apple')

#ejercicio 14
fruits = ("orange", "orange", "banana", "kiwi", "apple") #desde indice -4 (orange incluido), hasta -1 (apple excluido).
fruits[-4:-1] #('orange', 'banana', 'kiwi')

#ejercicio 15
fruits = ("orange", "orange", "banana", "kiwi", "apple")
if "kiwi" in fruits:
    print("kiwi is in fruits tuple")
# kiwi is in fruits tuple

#----------------------------
    
#ejercicio 16  
x = (1, 2)       #las tuplas al ser inmutables no permiten modificarlas, podemos convertirlas en listas modificar la lista y convertirla a tupla.
x = list(x)
x.append(3)
x = tuple(x)
# (1, 2, 3)




