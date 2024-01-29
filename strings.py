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
print(a[1])                            
print(a[1])                          #los strings en python se pueden tratar como una lista.     
                                    
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
print(a[2:8])                     #desde el indice 2 hasta el 8 sin incluirlo
print(a[:8])                      #desde inicio.
print(a[2:])                      #hasta final 
#ejercicio 11
x = "hello, world"                #con los indices negativos es de derecha a izquierda pero desde -1.
print(x[-5:-1])                   #desde la posicion -5(w), hasta la pos -1(d) sin tomarla.

#ejercicio 12
x = "hello, world"                #se puede usar el metodo upper() para poner en mayusculas el string.
print(x.upper()) 

#ejercicio 13
x = "HELLO, WOLRD"                #viceversa con el metodo lower().
print(x.lower())

#ejercicio 14
x = " hello, world "              #remover espacios en blanco en el comienzo y/o en el final.       
print(x.strip())

#ejercicio 15
x = "hello my friend"             #metodo .replace() para remplazar un string por otro.   
print(x.replace("m","n"))

#ejercicio 16
x = "Hola my bro, como estas,no te olvides de..."   #metodo para separar un string en varios substring.
print(x.split(","))

#ejercicio 17
a = "Hello, "
b = "worlds"                #se puede concatenar los strings con +.
c = a + b
print(c)

#ejercicio 17
a = "Hello,"
b = "worlds"                
c = a + " " + b
print(c)

#ejercicio 18
nombre = "Juan"
txt = "Hello, im {}, and im 18 years old"   #metodo que permite concatenar diferentes tipos de datos.
print(txt.format(nombre))

#ejerciio 19
price = 125.50
quantity = 10
quality = 5
txt = "Hi, i want a product of quality {}, price {} and quantity {}"
print(txt.format(quality, price, quantity))

#ejercicio 20
txt = "Texto para prueba de \"comillas\"." 
print(txt)

txt = "it\'s nice"
print(txt)

txt = "this will insert one \\ (backlslash)"
print(txt)

txt = "Example for\n     a new line" #toma los espacios despues de la n.
print(txt)

txt = "Hello \r World!"
print(txt) 

txt = "tab\t example"
print(txt) 

txt = "backspace \bexample"     #retrocede por decirlo asi un caracter(borra), pero solo se ve reflejado en la consola.
print(txt) 

txt = "form feed \fexample"     #es usado como para saltar de una pagina a otra, o para grandes espacios.
print(txt) 

txt = "octal value example \123\352\332" #muestra la letra correspondiente despues de cada \.
print(txt) 

txt ="hex value example \x45\xff\x8a" #igual pero usando un metodo diferente
print(txt) 

#ejercicio 20
x = "...string methods example..."

print(x.upper())               #todo a mayusculas.
print(x.lower())               #todo a minusculas.
print(x.capitalize())          #primera letra a mayuscula.
print(x.title())               #primera letra de cada palabra a mayuscula.
print(x.strip("."))               #elimina espacios en blanco al comienzo y al final, se puede especificar

x = ("Jhon", "11", "tall")     #para unir una tupla o cadena. Importante: solo debe cotener strings.
y = ",".join(x)
print(y)

x = "...string methods example..."  

print(x.find("example"))       #encuentra la posicion del primer index de la frase seleccionada en el string
print(x.startswith("...str"))       #verifica si la cadena inicia con cierto caracter o palabras
print(x.endswith("example..."))     #lo contrario al starswith