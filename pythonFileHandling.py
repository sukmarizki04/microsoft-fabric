print("====Python File Handling ====")
with open("myText.txt") as file:
    for line in file:
        print(line)

print("With line Number")
file = open('myText.txt', 'r')
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))