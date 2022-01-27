n, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

aList.sort()
bList.sort(reverse=True)

for i in range(k):
    if bList[i] > aList[i]:
        tmp = aList[i]
        aList[i] = bList[i]
        bList[i] = tmp
tmp = 0
for i in aList:
    tmp += i
print(tmp)
'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
