num = 10 
if num < 11 :
    print("it's true")
elif num > 11:
    print("Flase answer")
else:
    print("disclose") 
value = True
if not value:
    print("Value is false")
elif value is None:
    print("Value is None")
else:
    print("value is True")
print("=======Python Loops=====")
primes = [2,3,5,7]
for rime in primes:
    print(rime)
print("===With Index===")
nameAnimals = ["dog", "cat","mouse"]
for i,value in enumerate(nameAnimals):
    print(i,value)
print("===using while====")
x = 0
while x < 4:
    print(x)
    x+=1
print("===Pengunaan break====")

bBreakNumber = 0
for index in range(10):
    bBreakNumber = index * 10
    if index == 5:
        break
    print(x)

print("use continue in python")
for index1 in range(3,3):
    x = index1 * 10
    if index1 == 5:
        continue
    print(x)