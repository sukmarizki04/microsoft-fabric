import heapq
from collections import deque


myListData = [9,5,4,1,3,2]
heapq.heapify(myListData)
print(myListData)
print(myListData[0])

heapq.heappush(myListData, 10)
x = heapq.heappop(myListData)
print(x)
## Second in python advanced data types
print("Second in python advanced data types")
myListData = [9,5,4,1,3,2]
myListData = [-val for val in myListData]
heapq.heapify(myListData)
a  = heapq.heappop(myListData)
print(-a)

#Stack and queues

q = deque() #is empty data 
q = deque([1,2,3,4])

q.append(4) # insert append right side 
q.appendleft(0)
print(q) # q => be came (0,1,2,3,4)

x1 = q.pop() # remove and return from right 
y2 = q.popleft # remove and return from left 
print(x1)
print(y2)
print(q)

q.rotate(1) # rotate 1 step  to the right 
print(q)


