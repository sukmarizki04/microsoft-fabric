hello = "Hello World"
print(hello[1])
print(hello[-1])

# looping strings
print("\n")
for char in "Sukma":
    print(char)
# Panjang bagian string yang akan di olah 
hello1 = "Hello, world!"
print(len(hello1))

#Multiple Copies 
s = '===+'
n = 8
s * n
#string Checking  
a = 'spaw'
a in 'I spaw spam lot'
a not in 'afajfbjasfba'
# Concatenates 
concatenates = 'spam'
egg = 'egg'
concatenates + egg

# Formatting string 
# Memformat panjang string
name = "jhony"
print("Hello, %s!" % name)

name = "Jhony"
age = 10
print("%s is %d year old." % (name, age))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age= 36)
txt1 = "My name is {0}, I'm {1}".format("John", 36)
txt1 = "My name is {}, I'm {}".format("John",36)

# Slicing string in python
slicing = "they have one best motivated"
print(slicing[2:5])
print(slicing[0:2])
print(slicing[:2])
print(slicing[2:])
print(slicing[:2] + slicing[:2])
print(slicing[:])
print(slicing[-5:-2])
print(slicing[2:6])

myNumber = '12124314513' * 10
print(myNumber)
print(type(myNumber))
#Input something else
name1 = input('my name....')
# Join for the string 
"""
>>> "#".join(["John", "Peter", "Vicky"])
'John#Peter#Vicky'
"""
word = "Hello, world!".endswith("!")
print(word)
