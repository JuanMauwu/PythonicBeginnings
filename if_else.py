#ejercicio 1     tener presente la identación.
a = 100
b = 50

if a > b:
    print("si, 'a' es mayor que b.")
# si, 'a' es mayor que b.
    
#ejercicio 2    #se usa elif, si la condicion previa no es verdadera se intenta con otra.
a = 100
b = 50

if a < b:
    print("'a' es menor a b.")
elif a > b:
    print("'a' es mayor a b.")

#ejercicio 3   #else, si ninguna de las anteriores se cunmple entra al else y acaba.
a = 50
b = 50

if a < b:
    print("'a' es menor a b.")
elif b > a:
    print("'a' es mayor a b.")
else:
    print("'a' no es ni mayor, ni menor que b.")

#ejercicio 4       se puede usar el else sin haberse utilizado el elif.
a = 50
b = 50

if a > b:
    print("'a' es mayor que b.")
else:
    print("a no es mayor que b.")    
# a no es mayor que b
    
#ejercicio 5  # si solo se tiene una declaracion se puede poner en la misma linea del if. Sin else.
a = 50
b = 50

if a == b: print("'a' es igual a b.")
# 'a' es igual a b.

#ejercicio 6   si se quiere usar el else primero la accion, luego if condicion y por ultimo el else pero sin dos puntos.
a = 100
b = 2

print("x") if a == b else print("y")  #operadores ternarios.
# y

#ejercicio 7  se pueden poner mas condiciones, como si se usara elif.
a = 100
b = 2

print("x") if a == b else print("y") if a < b else print("z") 
# z

#ejercicio 8   unsado el operador logico and y operadores ternarios. 
a = 100
b = 50
c = 50

print("x") if b == c and a < b else print("y")
# y

# o usando la forma normal con el and.

if b == c and a < b:
    print("x")
else:
    print("y")
# y