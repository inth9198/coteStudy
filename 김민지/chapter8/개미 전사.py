# 9분 12초

n = int(input())
k = list(map(int, input().split()))

arr = [0]*n
arr[0], arr[1] = k[0], max(k[0], k[1])

for i in range(2, n):
  caseOne = k[i]+arr[i-2]
  caseTwo = arr[i-1]

  arr[i] = max(caseOne, caseTwo)

print(arr[-1])  