# ejercicio 1     sintaxis de funcion, en este caso sin valor de retorno:
def funcion():
    print("hello, world")

#ejercicio 2       #llamar la funcion, su nombre con dos parentesis.
def funcion():
    print("hello, world")
    
funcion() #hello, world

#ejercicio 3              #argumentos.
def fun_argumento(nombre):
    print("Hola", nombre)

fun_argumento("Juan")       #Hola Juan
fun_argumento("Pedrito")    #Hola Pedrito

#ejercicio 4               #función con varios argumentos o parametros.
def nombre(fname,lname):
    print("Hola",fname,lname)

nombre("Juan","Manuel") #Hola Juan Manuel

#ejercicio 4               #error al hacer el llamado sin los argumentos necesarios.
def nombre(fname,lname):
    print("Hola",fname,lname)

nombre("Juan") #TypeError: nombre() missing 1 required positional argument: 'lname'

#ejercicio 5
def my_function(*name):      #usamos asterisco para permitir que la funcion pueda disponer si es necesario de varios argumentos.
    print("Nombre:",name[1])

my_function("Juan", "Pedrito", "Carlitos")
#Nombre: Pedrito

#ejercicio 6
def function(niño1, niño2, niño3):
    print("El niño mas joven es:",niño3)

function(niño3="Juan", niño2="Pedrito", niño1="Carlitos")
#El niño mas joven es: Juan

#ejercicio 7
def my_function(**kid):                     #si no sabemos el numero de palabras claves que tendremos como argumento **.
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#ejercicio 7
def func(pais = "Colombia"):   #se le puede pasar el valor predeterminado al argumento. Si no se especifica se usa.
    print("Soy de", pais)

func()
func("Peru")
func("Ecuador")
#Soy de Colombia
#Soy de Peru
#S oy de Ecuador

#ejercicio 8
def funcion_recorrer(comida):     #mandando lista como argumento
    for x in comida:
        print(x)

frutas = ["Pera", "Mango", "kiwi"]

funcion_recorrer(frutas)
#Pera
#Mango
#kiwi

#ejercicio 9
def funcion_retorno(x):  #valor de retorno predeterminado con declaracion return
    return 10 * x

funcion_retorno(5)
#50

#ejercicio 10        si por alguna razon queremos una funcion sin contenido debemos agregar pass.
def myfunction():
  pass

#ejercicio 11
def my_function(x, /):       
  print(x)

my_function(3) #3            #si se agrega ",/" la funcion no permitira argumentos tipo clave=dato
my_function(x = 3)           #TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'


#ejercicio 12
def my_function(*, x):      #para especificar que el argumento entre con clave-valor.
  print(x)

my_function(x = 3) #3
my_function(3)             #TypeError: my_function() takes 0 positional arguments but 1 was given

#ejercicio 13
def my_function(a, b, /, *, c, d):   #se pueden combinar:( a y b sin clave-valor), (c y d con clave-valor)
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8) #26

#ejercicio 14
def tri_recursion(k):   #recursion 
  if k > 0:
    result = k + tri_recursion(k - 1)   
    print(result)
  else:     
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#ejercicio 15   sobre factorial usando recursion. 
def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n - 1) #factorial de 5 es = 5*factorial de 4, pero factorial de 4 es = 4*factorial de 3.....
                                  #5*4*3*2*1
factorial(5) #120

#-------------------------------------------
#Funciones lambda
#No necesitas definirla con un nombre(anonimas)
#Ideal para definir funciones pequeñas

#Sintaxis-->   lambda aguments : expression

#ejercicio 16
x = lambda n : n + 5
x(5) #10

#ejercicio 17
suma = lambda x, y : x + y   #con varios argumentos
suma(10,20) #30

#Ejercicios implementando estructuras de python.

"""
1.Crea una función que genere una lista de números del 1 al 10 y otra que impirma esa lista.
"""

numbers = []

def add_numbers(list):
   x = 0
   while x < 10:
    list.append(x + 1)
    x +=1

def print_list(list):
   for x in list:
      print(x)

add_numbers(numbers) #se llena la lista
print_list(numbers)  #se imprime la lista
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

"""
2.Crea una función que llene un diccionario donde las claves sean los nombres de tus amigos y los 
valores sean sus edades. Luego debe que debera imprimir el nombre y la edad de cada amigo.
"""

def new_dictionary():
    friends = {
        "Pedrito": 12,
        "Carlitos": 32,
        "Fulanito": 16
    }
    
    for name, age in friends.items():  #se usa el metodo de los diccionarios items()
       print(name, age)

new_dictionary()
#Pedrito 12
#Carlitos 32
#Fulanito 16

# items()	    Returns a list containing a tuple for each key value pair
