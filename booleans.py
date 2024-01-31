#ejercicio 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#ejercicio 2
x = 100
y = 50
if x > y:
    print("x es mayor a y")
else:
    print("x no es mayor a y")     

#ejercicio 3
print(bool("Hello"))
print(bool(""))         #cuando la cadena esta vacia devuelve false
print(bool(15))
print(bool(0))          #cuando es 0 devuelve false

#ejercicio 4
x = "Hello"
y = 0
print(bool(x))
print(bool(y))

#ejercicio 5
x = bool(["", 123, 124.124124]) #cualquier lista-tupla-diccionario-set seran true a menos que esten vacios comletamente.
y = bool({})
print(x)          #devuelve true.
print(y)          #devuelve false.

#ejercicio 6
print(bool(""))
print(bool(0))
print(bool(()))
print(bool([]))         #esto se evalua en false.
print(bool({}))         #aparte hay un metodo especial pero tiene que ver con clases "__len__"
print(bool(False))
print(bool(None))

#ejercicio 7
def saludar():          #las funciones pueden devolver un booleano tambien
    return True

print(saludar())

#ejercicio 8
def funcion():
    return True

if funcion():
    print("la funcion retorna True")
else:
    print("La funcion retorna False")    

#ejercicio 9
x = "Hello" 
print(isinstance(x, int))   #funcion que devuelve un boolean segun el tipo de dato