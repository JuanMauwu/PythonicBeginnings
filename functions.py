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
def my_function(**kid):
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
def my_function(*, x):      #para especificar que el argumento entre con calve-valor.
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