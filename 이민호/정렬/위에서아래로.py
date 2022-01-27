n=int(input())
myList = []
for i in range(n):
    myList.append(int(input()))
myList.sort(reverse=True)
for i in range(n):
    print(myList[i], end=' ')
