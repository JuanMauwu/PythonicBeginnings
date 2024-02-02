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

#ejercicio 4
names = ["Juan", "Sebastian", "Luisa", "Juan"]
numbers = [1, 2 ,3 ,4]                          #una lista puede ser de cualquier tipo de dato.
lista = [True, False, False]

#ejercicio 5
variado = ["Juan", 1, 2.5, False]  #las listas pueden contener diferentes tipos de datos.

#ejercicio 6
lista = ["Juan", 1, 2.5, False]  #es definido como tipo dato list.
print(type(list))

#ejercicio 6
animales = list(["perro", "gato","pajaro"]) #tambien se puede utilizar un constructor para crear una lista.

#ejercicio 7
fruits = ["banana", "apple", "orange", "banana"]
print(fruits[1])                                       #acceder y muestra el segundo item de la lista.

#ejercicio 8
fruits = ["banana", "apple", "orange", "banana"]       #si se usa el negativo comienza de derecha a izquierda desde -1.
print(fruits[-1])

#ejercicio 9
fruits = ["banana", "apple", "orange", "banana"] 
print(fruits[0 : 2])                                   #para seleccionar ciertos elementos en especificos sin tomar el ultimo
#['banana', 'apple']