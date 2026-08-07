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