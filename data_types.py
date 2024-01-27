#ejercicio 1
x = 10
print(x)  #para imprmir el tipo de variable

#ejercicio 2
a = "hello"    #string
print(a)
print(type(a))

b = 100        #int
print(b)
print(type(b))

c = 25.5       #float
print(c)
print(type(c))

d = 100j       #complex (complejo)
print (d)
print(type(d))

e = [1, 1.5, "hola", True, False] #list (se puede modificar despues de su declaracion)
print(e)
print(type(e))

f = (1, 1.5, "hello", True, [1, 2, 3]) #tuple (lo mismo que la lista, NO es mutable y es con())
print(f)
print(type(f))

g = range(5)   #range (es una funcion para generar una secuencia de numeros en cierto rango)
print(g)
print(type(g))

h = {"Nombre" : "Juan", "Edad" : 18} #dict (es por decirlo asi una variable que guarda otras variables con sus datos)
print(h)
print(type(h))

i = {1, 2, 3, "a" ,"b"}  #set (un conjunto pero no esta ordenado con indices,no permite datos repetidos, 
print(i)                 #es mutable y puede contener varios tipos de datos )              
print(type(i))

j = frozenset({1 ,2 ,1.4,"a", "b"}) #frozenset (lo mismo que el set pero NO es mutable)
print(j)
print(type(j))

k = True       #bool (booleano)
print(k)
print(type(k))

l = b"hi"      #bytes (una forma de representar datos binarios)
print(l)
print(type(l))

m = bytearray(6)
print(m)
print(type(m))

n = memoryview(bytes(5))
print(x)
print(type(n)) 

ñ = None
print(ñ)
print(type(ñ))