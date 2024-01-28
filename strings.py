#ejercicio 1
print('hello')
print("hello")

#ejercicio 2
a = "hello"
print(a)

#ejercicio 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed        
do eiusmod tempor incididunt ut 
labore et dolore magna aliqua."""    #""" o ''' para crear un string multilinea.
print(a)

#ejercicio 4
a = "Hello, world"
print(a[0])         
print(a[1])                          #los strings en python se pueden tratar como una secuencia de caracteres (array).     
                                    
#ejercicio 5
fruit = "Banana"

for x in fruit:
    print(x)

#ejercicio 6
x = "Hello my bro"      #función len para conocer el tamaño del string. 
print(len(x))

#ejercicio 7            #se puede usar la keyword in para conocer si hay cierta palabra o frase en un string.
x = "hello, world"
print("hello" in x)

#ejercicio 8
x = "hello, world"
if "world" in x:
    print("Yes world is in x") 

#ejercico 9
x = "Hello, man"
print("world" not in x)           #in not para saber si no esta. Funciona igual con el if.

#ejercicio 10
a = "Hello, world"                #slicing o rebanar un string.
print(a[2:8])
print(a[:8])                      #desde inicio.
print(a[2:])                      #hasta final.

#ejercicio 11
x = "hello, world"                #con los indices negativos es de derecha a izquierda pero desde -1.
print(x[-5:-1])                   #desde la posicion -5(w), hasta la pos -1(d) sin tomarla.

#ejercicio 12
x = "hello, world"                #se puede usar el metodo upper() para poner en mayusculas el string
print(x.upper()) 

#ejercicio 13
x = "HELLO, WOLRD"                #viceversa con el metodo lower()
print(x.lower())

#ejercicio 14
x = " hello, world "               #remover espacios en blanco en el comienzo y/o en el final       
print(x.strip())

#ejercicio 15