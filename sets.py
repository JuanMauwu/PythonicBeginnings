#ejercicio 1
new_set = {"banana", "cherry", "watermelon"} #los sets no estan ordenados.

#ejercicio 2
new_set = {"banana", "cherry", "watermelon", "cherry"} #los elementos duplicados seran ignorados.
print(new_set)           
#{'banana', 'watermelon', 'cherry'}

#ejercicio 3
set = {'banana', 'watermelon', 'cherry', True, 1} #True y 1 en los sets valen lo mismo. Se puede ver que el set al imprimirlo aparece EN DESORDEN
print(set)                                        #Igual el 0 y el False.
#{'cherry', True, 'banana', 'watermelon'}

#ejercicio 4
new_set = {"banana", "cherry", "watermelon"}    #funcion len() para saber el numero de indices de la tupla.
len(new_set)
#3

#ejercicio 5
variado = {"hello", 1, 1.5, False, True} #permite contener varios tipos de datos.

#ejercicio 6
variado = {"hello", 1, 1.5, False, True} #funcion type() devuelve set.
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
new_set = ["banana", "cherry", "watermelon"]    #metodo update() sirve para agregar elementos de otro iterable.
numbers.update(new_set)
#{1, 2, 3, 4, 'banana', 'cherry', 'watermelon'}

#ejercicio 12       #metodo intersection() para crear una nueva tupla con los valores presentes en x y Y.
x = {1,2,3}
y = {1,4,5,6}
z = x.intersection(y)
# {1}

#ejercicio 13
x = {"apple", "banana", "lemon"}    # A x se le dan los elementos de que no esten presentes tanto en x como en y.
y = {"google", "kiwi", "apple"}
x.symmetric_difference_update(y)
print(x) #{'lemon', 'kiwi', 'google', 'banana'}

#ejercicio 14
x = {"apple", "banana", "cherry"}  # metodo symmetric_difference(), pero este sirve para crear otra variable.
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
#{'google', 'cherry', 'banana', 'microsoft'}

#----------------------------

#add()	         Adds an element to the set
#clear()	     Removes all the elements from the set
#copy()	         Returns a copy of the set
#difference()	 Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	     Remove the specified item
#intersection()	 Returns a set, that is the intersection of two other sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	 Returns whether two sets have a intersection or not
#issubset()	     Returns whether another set contains this set or not
#issuperset()	 Returns whether this set contains another set or not
#pop()	         Removes an element from the set
#remove()	     Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	     Return a set containing the union of sets
#update()	     Update the set with the union of this set and others



