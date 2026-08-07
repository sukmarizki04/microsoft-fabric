x = 0
for index in range(3,8):
    x = index * 10
    if index == 5:
        continue
    print(x)
print("Using range in python")
for i in range(10):
    print(i)
print("Start for 4")
for i in range(4,10):
    print(i)
print("Working with zip")
words = ["Mon", "Tues", "Wed"]
nums = [1,2,3]
for w, n in zip(words, nums):
    print('%d:%s, ' %(n, w) )
print("==== For/Else ===")
nums = [60,30,70,110, 90]
for n in nums:
    if n > 100:
        print("%d is bigger than 100" %n)
        break
    else:
        print("Not Found!")