# 13분 28초

n, m = map(int, input().split())
value = []
for i in range(n):
  value.append(int(input()))

arr = [10001]*(m+1)
for v in value:
  i = 1
  while (v*i)<=m:
    arr[v*i] = min(arr[v*i], i)
    i += 1

result = 10001
for i in range(1, m+1):
  result = min(result, arr[i]+arr[m-i])

if result==10001:
  print(-1)
else:
  print(result)