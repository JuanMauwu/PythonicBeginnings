#ejercicio 1
i = 0
while i < 3:
    print(i)
    i+=1
# 0
# 1
# 2
    
#ejercicio 2   si usamos palabra clave break, para tanto el if como el while.  
i = 0

while i < 5:
    print(i)

    if i == 3:
        break

    i+=1
# 0
# 1
# 2
# 3
    
#ejercicio 3    continue pasa directamente a la siguiente iteracion del bucle. Vemos que el segundo print jamas se ejecuta.
i = 0
while i < 5:
    print(i)
    i += 1
    if i <= 5:
        continue
    print("esto no se imprimira")
# 0
# 1
# 2
# 3
# 4
    
#ejercicio 4    se puede usar el else y se ejecuta cuando la condicion no se cumpla.
i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("i no es mayor a 0")
# 5
# 4
# 3
# 2
# 1
# i no es mayor a 0