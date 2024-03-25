#ejercicio 1
class NewClass:  #nombre en CamelCase iniciando con  mayuscula.
    x = 5

obj = NewClass() #se crea una INSTANCIA del nuevo objeto.
print(obj.x)
#5

#ejercicio 2
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Persona("Juan", 18)
print(p1.name) 
print(p1.age)
#Juan
#18