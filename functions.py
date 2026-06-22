

def nameFunction():
    print("Hello  from a function ")
#File Handling 
with open("myfile.txt","r", encoding="utf8") as file :
    for line in file:
        print(line)
#aritmetics 
result1 = 10 + 30
result2 = 40 - 50
result3 = 50 * 5
result4 = 16 / 4 
result5 = 16 // 4
result6 = 25 % 2
result7 = 5 ** 2
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

# Plust- Equals 
counter = 0
counter += 1

counterResult =  counter + 10 
message = " part one"
message += " part two"

