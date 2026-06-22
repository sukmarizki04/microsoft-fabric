import heapq

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