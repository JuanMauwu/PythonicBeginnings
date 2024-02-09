#ejercicio 1
new_set = {"banana", "cherry", "watermelon"} #los sets no estan ordenados.

#ejercicio 2
new_set = {"banana", "cherry", "watermelon", "cherry"} #los elementos duplicados seran ignorados.
print(new_set)           
#{'banana', 'watermelon', 'cherry'}

#ejercicio 3
set = {'banana', 'watermelon', 'cherry', True, 1} #True y 1 en los sets valen lo mismo. Se puede ver que el set al imprimirlo aparece en otro orden
print(set)                                        #Igual el 0 y el False.
#{'cherry', True, 'banana', 'watermelon'}

#ejercicio 4
new_set = {"banana", "cherry", "watermelon"}    #funcion len() para saber el numero de indices de la tupla.
len(new_set)
#3

#ejercicio 5
variado = {"hello", 1, 1.5, False, True} #permite contener varios tipos de datos.

#ejercicio 6
variado = {"hello", 1, 1.5, False, True} #funcion tupe() devuelve set.
type(variado)
# <class 'set'>

#ejercicio 7
variado = tuple({"hello", 1, 1.5, False, True}) #contructor de la tupla-

#----------------------------

#ejercicio 8
variado = tuple({"hello", 2, 1.5, False, True}) #con las tuplas no podemos acceder a los elementos po el indice, toca po bucles o usando condicionales.
for x in variado:
    print(x)
#False
#1.5
#2
#True
#hello

#ejercicio 9
variado = tuple({"hello", 2, 1.5, False, True}) #verificar si un elemento en particular se encuentra en el set.
print(2 in variado)
#True

#-----------------------------

#ejercicio 10 "Un set no permite modificar sus elementos pero si agregar"
numbers = {1, 2, 3, 4}  
numbers.add(1000)           #usar metodo add() para agragar elementos
#{1, 2, 3, 4, 1000}

#ejercicio 11
numbers = {1, 2, 3, 4}          
new_set = ["banana", "cherry", "watermelon"]    #metodo update() sirve para agragar elementos de otro iterable.
numbers.update(new_set)
#{1, 2, 3, 4, 'banana', 'cherry', 'watermelon'}

#----------------------------

#ejercicio 12
