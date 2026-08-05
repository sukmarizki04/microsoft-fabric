
#Defining List 
li1 = []
li1
[]
li2 = [4, 5, 6]
li2
[4, 5, 6]
li3 = list((1, 2, 3))
li3
[1, 2, 3]
li4 = list(range(1, 11))
li4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Generate List in Python 
list(filter(lambda x : x % 2 == 1, range(1, 20)))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[x ** 2 for x in range (1, 11) if  x % 2 == 1]
[1, 9, 25, 49, 81]
[x for x in [3, 4, 5, 6, 7] if x > 5]
[6, 7]
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
[6, 7]

#Append in form List 
li1 = []
li1.append(1)
li1
[1]
li1.append(2)
li1
[1, 2]
li1.append(4)
li1
[1, 2, 4]
li1.append(3)
li1
[1, 2, 4, 3]

#List Method Slicing in python 
# a_list1[start:end]
# a_list1[start:end:step]

## REMOVE METHOD LIST 
li2 = ['bread', 'butter', 'milk']
li2.pop()
'milk'
li2
['bread', 'butter']
del li2[0]
li2
['butter']

## OMITTING INDEX 
# aaA[:4]
# ['spam', 'egg', 'bacon', 'tomato']
# aaA[0:4]
# ['spam', 'egg', 'bacon', 'tomato']
# aaA[2:]
# ['bacon', 'tomato', 'ham', 'lobster']
# aaA[2:len(a)]
# ['bacon', 'tomato', 'ham', 'lobster']
# aaA
# ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# aaA[:]
# ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

# Acces List in python 
liA = ['a', 'b', 'c', 'd']
liA[0]
'a'
liA[-1]
'd'
liA[4]
## With Stride 
deretList = ['spam', 'egg', 'bacon', 'tomato', 'ham','lobster']
deretList[0:6:3]

#concatenating 
odd = [1,3,5]
odd.extend([9,1,6])
print(odd)


#Sort and Reverge 
ListA = [3,1,3,2,5]
ListA.sort()
print(list)
ListA.reverse()
