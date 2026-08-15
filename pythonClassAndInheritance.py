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
    def print(test):
        print("Parent Method")
