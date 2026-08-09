def hello_Word():
    print("This Function Hello World")
print("====Value Return Function===")
def sum(a,d):
    if a <= 50:
        c = a * 20
        print(c)
    return a + d + c
print(sum(10,20))
print("=== Positional Arguments ===")
def varags(*args):
    return args
print(varags(10,20,30))

print("=== Keywords Arguments ===")
def keywords_args(**kwargs):
    return kwargs
keywords_args(big="foot", loch = "ness")

print(" Returning multiple ")
def swap(x,y):
    return x,y
x = 1
y = 2
x,y = swap(x,y)
print("====Default Value===")
def add1(x, y= 10):
    return x + y
add1(10)
add1(5, 10)
print(add1(10,30))

print("=== Anonymous Function====")
print((lambda x : x > 2)(3))
print((lambda x,y : x ** 2 + y ** 2)(2,1))