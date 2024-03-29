#ejercicio 1
class NewClass:  #nombre en CamelCase iniciando con  mayuscula.
    x = 5

obj = NewClass() #se crea una INSTANCIA del nuevo objeto.
print(obj.x)
#5

#ejercicio 2
class Persona:
    def __init__(self, name, age):  #constructor
        self.name = name
        self.age = age

p1 = Persona("Juan", 18)
print(p1.name) 
print(p1.age)
#Juan
#18

#ejercicio 3
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):                       #funcion o metodo especial para representar un objeto como un string.
        return f"{self.name}({self.age})"  
    
p1 = Persona("Juan", 18)
print(p1)
# Juan(18)

#ejercicio 4
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def tell_name(self):                #metodo(funcion que pertenece al objeto).
        print("My name is "+self.name)

p1 = Persona("Juan", 18)
p1.tell_name()
# My name is Juan   

#ejercicio 5
class Person:
  def __init__(mysillyobject, name, age):   #se puede usar mysillyobject y abc en lugar de self.
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#Hello my name is John

#ejercicio 6
class Persona:
    def __init__(self, name, age):  #modificar un atributo.
        self.name = name
        self.age = age

p1 = Persona("Juan", 18)
p1.age #18

p1.age = 19
p1.age #19

#ejercicio 7
class Persona:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

p1 = Persona("Juan", 18)   #palabra clave "del" para borrar un atributo, se puede hacer tambine para un objeto completo.
del p1.age
p1.age     #AttributeError: 'Persona' object has no attribute 'age'
 
#ejercicio 8
class Person:  #si por alguna razon se necesita una clase vacia se debe usar pass para evitar unn error.
  pass

#ejercicio 9 "herencia" 
class Person:                         #clase padre.
    def __init__(self, fname, lname): 
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)

class Student(Person):                      #clase hija que hereda de Person los stributos fname, lname y el metodo print_name().
    def __init__(self,fname,lname, grade):  #primero los atributos que hereda y luego el propio(grade).
        super().__init__(fname, lname)      #se utiliza la funcion super() para llamar al constructor de la clase padre.
        self.grade = grade                  #por ultimo se le asigna el valor a los atributos propios de la clase hija.

student1 = Student("Juan", "Velásquez", 11)
student1.print_name()                         #hereda fname, lname y el metodo print_name().
# Juan Velásquez