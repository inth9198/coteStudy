# 11분 37초

n = int(input())

arr = [0]*1001
arr[1], arr[2] = 1, 3

for i in range(3, n+1):
  arr[i] = (arr[i-1]+(arr[i-2]*2))%796796
  
print(arr[n])