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

#extra
a = 100
b = 50
if a > b:
    print("1")
elif a >= b:
    print("2")
# 1
# en este caso ambas sentencias son correctas, pero solo se aplica la primera.

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

#ejercicio 8   unsado palabra clave and. Todo debe ser verdad para que arroje verdadero. 
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
    
#ejercicio 9  palabra clave or, si una es verdadera todo da verdadero
a = 100
b = 50
c = 50

if a < b or a > c:
    print("nice")
# nice
    
#ejercicio 10   la palabra clave "not" niega el resultado de la sentenca. True => False y viceversa
a = 100
b = 50
#esta sentencia da False, pero con "not" se convierte en True y se ejecuta la instruccion.
if not b > a:        
    print("nice")
# nice

# ejercicio 11          if anidado.
a = 100

if a > 10:
    print("mayor a 10")
    if a > 50:
        print("mayor a 50")
    else:
        print("menor a 50")
#mayor a 10
#mayor a 50

#ejercicio 12   si por alguna razon queremos un if sin contenido agragamos pass.
a = 100
b = 50

if a > b:
    pass

a = 100
b = 50
if a > b:
    print("1")
elif a >= b:
    print("2")