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

#ejercicio 4               #error al hacer el llamado si los argumentos necesarios.
def nombre(fname,lname):
    print("Hola",fname,lname)

nombre("Juan") #TypeError: nombre() missing 1 required positional argument: 'lname'

#ejercicio 5
