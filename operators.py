#ejercicio 1
print(1 + 1)

#ejercicio 2
x = 5
y = 2

print(x + y)    #OPERADORES ARITMETICOS
print(x - y)
print(x * y)
print(x / y)
print(x % y) #residuo de dividir x por y.
print(x ** y) #potencia x a la y.
print(x // y)

#ejercicio 3
x = 10          #OPERADORES DE ASIGNACION
x += 5
print(x)

x = 10
x -= 5
print(x)

x = 10
x *= 5
print(x)

x = 10
x /= 5
print(x)

x = 10
x %= 3
print(x)

x = 10
x //= 3
print(x)

x = 10
x **= 3
print(x)

x = 10
x &= 3      #una operacion con numeros binarios.
print(x)

x = 10
x |= 3      #con bits.
print(x)

x = 10
x >>= 3     #bits.
print(x)

x = 10
x <<= 3     #bits.
print(x)

#ejercicio 4
X = 10                #OPERADORES DE COMPARACION
Y = 5

print(10 == 5)
print(10 != 5)
print(10 > 5)
print(10 < 5)          #compara y devuelve un booleano.
print(10 >= 5)
print(10 <= 5)

#ejercicio 5
x = 10                #OPERADORES LOGICOS        
y = 5

if x > 1 and y > 1:                       #el and solo devolvera True si ambas expresiones son True.
    print("X y Y son mayores a 1")

if x > 1 or y < 1:
    print("X es mayor a 1 pero Y no")     #el or solo devuelve False si ambas son False.

print(not(x > 1 and y > 1))               #el not devuelve el resultado copntrario al que se obtuvo.

#ejercicio 6
x = [1, 2, 3]               #OPERADORES DE INDENTIDAD
y = [1, 2, 3]
z = x

print(x is y) #devuelve false, aunque X y Y tengan mismos datos no estan en igual lugar en memoria.
print(x is z) #devuelve true, ya que es la misma lista en memoria.

print(x is not y) #lo contrario al  IS. Devuelve true
print(x is not z) #devuelve false}

#ejercicio 7
fruits = ["apple", "banana"] #OPERADORES MEMBERSHIP
print("banana" in fruits)       # pregunta si algo esta o no esta presente o no en un objeto
print("banana" not in fruits)

#ejercicio 8
x = 5               #OPERADORES PARA NUMEROS BINARIOS
y = 2
print(x & y)
print(x | y)
print(x ^ y)
print(~ x)
print(x >> 2)
print(x << 2)

#ejercicio 9
print((6 + 6)*(3 - 1))     #los parentesis son los primeros en orden
print((1 + 1 * 2))         #prodcuto primero que la suma
print((1 + 1 - 4 + 5 - 6)) #la suma y la resta tienen la misma prededencia y se evalua de izquierda a dereche   
#los operadores con la misma jerarquia se evaluan de izquierda a derecha

#Jerarquia de los operadores:
# ()    parentesis
# **    exponencial
# +x  -x  ~x  	unary plus, unary minus, and bitwise NOT
# *  /  //  %   multiplication, division, floor division, and modulus
# +  -   addition and subtraction
# <<  >>  	Bitwise left and right shifts
# &  bitwise and
# |  bitwise or
# ==  !=  >  >=  <  <=  is  is not  in  not in  comparisons, identity, and membership operators
# not  logico not
# and  logico and
# or   logico or
