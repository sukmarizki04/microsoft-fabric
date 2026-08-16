#Defining class in python 

class MyNewClassname:
    print("mynewclass")
    pass

# Constractors class 

class Animal:
    def __init__(self, voice):
        self.voice = voice
cat = Animal("voice cat")
print(cat.voice) 

dog = Animal('Woof')
print(dog.voice)

# Method in python 
class Dog:
    def barf(self):
        print("ham-ham")
charlie = Dog()
charlie.barf  

#class inside the vaiable in python 
class VariableClass:
    classVariable = "A class variable!"
print(VariableClass.classVariable)
x = VariableClass()
print(x.classVariable)

#Super() Function
class ParentClass:
    def print_test(self):
        print("Parent Method")

class ChildClass(ParentClass):
    def print_test(self):
        print("Child Method")
        super().print_test()

#repr() method 
class Employee:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
john = Employee("Jhon Walker")
print(john)
# User definite Exception 
class CustomError(Exception):
    pass
#Polipmorphism 
class OldClass:
    def print_self(self):
        print('A')
class ChildClass(OldClass):
    def print_self(self):
        print('B')
objA = OldClass()
objB = ChildClass()
objA.print_self()
objB.print_self()
"""
Overriding 
"""
class ClassParent:
    def print_self(self):
        print("Parent")
class ChildClassParent(ClassParent):
    def print_self(self):
        print("Child")
child_Instance = ChildClassParent()
child_Instance.print_self()

#Inheritance
class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
class Dog(Animal):
    def sound(self):
        print('Woof!')
yoki = Dog("Yoki", 5)
print(yoki.name)
print(yoki.legs)
yoki.sound

