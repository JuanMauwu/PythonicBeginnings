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

#ejercicio 4                #funcion len para saber el numero de elementos de el diccionario.
carro = {                   
    "marca": "nissan",
    "año": 2005,
    "color": "azul"
}
len(carro)
# 3

#ejercicio 5            #puede contener cualquier tipo de dato.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

#ejercico 6                 #funcion type() para conocer el tipo de dato.
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

#ejercicio 8                    #obtener el valor de cierta clave en especifico.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario["electrico"]
# False

#ejercicio 9            #igual pero usando metodo para diccionarios get().
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario.get("año")
# 1980

#ejercicio 10           #metodo key() que devuelve las claves de nuestro diccionario.
diccionario = {
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}
diccionario.keys()
# dict_keys(['marca', 'electrico', 'año', 'color'])

#ejercicio 11               #añadir nueva clave.
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.keys()               # dict_keys(['marca', 'electrico', 'año', 'color'])

diccionario["tamaño"] = "grande"

diccionario.keys()               #dict_keys(['marca', 'electrico', 'año', 'color', 'tamaño'])

#ejercicio 12
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.values()
# dict_values(['toyota', False, 1980, ['red', 'blue', 'green']])

#ejercicio 13               #modificar los datos y usar metodo values().
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.values() #dict_values(['toyota', False, 1980, ['red', 'blue', 'green']])

diccionario["color"][1] = "black"

diccionario.values() #dict_values(['toyota', False, 1980, ['red', 'black', 'green']])

#ejercicio 14     #metodo items() me devuelve cada elemento(clave:dato)
diccionario = { 
    "marca": "toyota",
    "electrico": False,
    "año": 1980,
    "color": ["red", "blue", "green"]
}

diccionario.items()
# dict_items([('marca', 'toyota'), ('electrico', False), ('año', 1980), ('color', ['red', 'blue', 'green'])])

#ejercicio 15   #se puede usar las entencia de decision y la palabra clave in para determinar si la clave se encuentra. 
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

# si, la clave 'año' esta presente en el diccionario