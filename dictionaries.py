#ejercicio 1
carro = {                   # sintaxis de un diccionario. Es ordenado, modificable y no permite duplicados.
    "marca": "nissan",      #almacena valores en parejas (clave:valor).
    "año": 2005,
    "color": "azul"
}
print(carro) #{'marca': 'nissan', 'año': 2005, 'color': 'azul'}

#ejercicio 2
carro = {                   #refiriendose a un valor por su clave.
    "marca": "nissan",
    "año": 2005,
    "color": "azul"
}
carro["color"]
#'azul'

#ejercicio 3
carro = {                 #no permite mas d eun elemento con la misma clave. En este caso se reescribe el valor a negro.
    "marca": "nissan",
    "año": 2005,
    "color": "azul",
    "color": "negro"
}
carro["color"]
#'negro'

#ejercicio 4                #uncion len para saber el numero de elementos de el diccionario.
carro = {                   
    "marca": "nissan",
    "año": 2005,
    "color": "azul"
}
len(carro)
# 3

#ejercicio 5            puede contener cualquier tipo de dato.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

#ejercico 6                 funcion type() para conocer el tipo de dato.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
type(diccionario)
#<class 'dict'>

#ejercicio 7
diccionario = dict(name = "Juan", age = 18, city = "Jericó") #otra forma de crear un diccionario.
print(diccionario)
#{'name': 'Juan', 'age': 18, 'city': 'Jericó'}

#-----------------------------

#ejercicio 8                    obtener el valor de cierta clave en especifico.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario["electrico"]
# False

#ejercicio 9            igual pero usando metodo para diccionarios get().
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario.get("año")
# 1980

#ejercicio 10           metodo key() que devuelve las claves de nuestro diccionario.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario.keys()
# dict_keys(['marca', 'electrico', 'año', 'color']).

#ejercicio 11               añadir nueva clave.
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.keys()               # dict_keys(['marca', 'electrico', 'año', 'color']).

diccionario["tamaño"] = "grande"

diccionario.keys()               #dict_keys(['marca', 'electrico', 'año', 'color', 'tamaño']).

#ejercicio 12
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.values()
# dict_values(['toyota', False, 1980, ['red', 'blue', 'green']]).

#ejercicio 13               modificar los datos y usar metodo values().
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.values() #dict_values(['toyota', False, 1980, ['red', 'blue', 'green']]).

diccionario["color"][1] = "black"

diccionario.values() #dict_values(['toyota', False, 1980, ['red', 'black', 'green']]).

#ejercicio 14     metodo items() me devuelve cada elemento(clave:dato)
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.items()
# dict_items([('marca', 'toyota'), ('electrico', False), ('año', 1980), ('color', ['red', 'blue', 'green'])])

#ejercicio 15   se puede usar las entencia de decision y la palabra clave in para determinar si la clave se encuentra. 
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

if "año" in diccionario:
    print("si, la clave 'año' esta presente en el diccionario")
else:
    print("no, la clave 'año' no esta presente en el diccionario")

# si, la clave 'año' esta presente en el diccionario.
    
#----------------------------
    
#ejercicio 16                  modificar valores.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario["año"] = 2000
#{'marca': 'toyota', 'electrico': False, 'año': 2000, 'color': ['red', 'blue', 'green']}

#ejercicio 17       modificar valor pero usando metodo update({}).
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario.update({"marca":"nissan"})
# {'marca': 'nissan', 'electrico': False, 'año': 1980, 'color': ['red', 'blue', 'green']}

#----------------------------

#ejercicio 18
dict = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
dict["tamaño"] = "grande"
# {'marca': 'toyota', 'electrico': False, 'año': 1980, 'color': ['red', 'blue', 'green'], 'tamaño': 'grande'}

#ejercicio 19
dict = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
dict.update({"tamaño":"pequeño"})
# {'marca': 'toyota', 'electrico': False, 'año': 1980, 'color': ['red', 'blue', 'green'], 'tamaño': 'pequeño'}

#----------------------------

#ejercicio 19         el metodo pop() elimina el elemento entero con solo poner su clave.
dict = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
dict.pop("año")
# {'marca': 'toyota', 'electrico': False, 'color': ['red', 'blue', 'green']}

#ejercicio 20        metodo dict remueve el ultimo elemento añadido.
dict = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
dict.popitem()
# {'marca': 'toyota', 'electrico': False, 'año': 1980}

#ejercicio 21      la palabra clave del elimita el elemento especificando su clave.
dict = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
del dict["electrico"]
# {'marca': 'toyota', 'año': 1980, 'color': ['red', 'blue', 'green']}

#ejercicio 22       tener en cuenta que "del" puede eliminar el diccionario completo.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
del dic
print(dic)

#ejercicio 23    metodo clear() vacia pero NO elimina el diccionario.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
dic.clear()
print(dic)
# {}

#----------------------------

#ejercicio 24     usando los bucles de esta forma solo nos devolvera la clave del elemento.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

for x in dic:
    print(x)
# marca
# electrico
# año
# color
    
# ejercicio 25      en este caso de imprimen los valores de cada elemento.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

for x in dic:   #prueba: acceder a una lista de un dic e imprimir sus elementos.
    print(dic[x])
# toyota
# False
# 1980
# ['red', 'blue', 'green']

for x in dic["color"]:
    print(x)
#red
#blue
#green
    
#ejercicio 26     o simplemente usar el metodo values() y asi recorrer y tomar los valores de cada elemento.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
for x in dic.values():
    print(x)
#toyota
#False
#1980
#['red', 'blue', 'green']

#ejercicio 27    si se usa el metodo key() se obtienen las claves de los elementos.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
for x in dic.keys():
    print(x)
#marca
#electrico
#año
#color
    
#ejercicio 28   se usa el metodo items() para obtener tanto la clave como el valor del elemento del diccionario.
dic = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
for x, y in dic.items():
    print(x, y)
# marca toyota
# electrico False
# año 1980
# color ['red', 'blue', 'green']