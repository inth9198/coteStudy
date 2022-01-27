n=int(input())
myList = []
for i in range(n):
    tmp=input().split()
    myList.append((tmp[0], int(tmp[1])))
myList = sorted(myList, key=lambda a: a[1])
for i in myList:
    print(i[0],end=' ')
