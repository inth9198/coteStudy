# 10분

n, m = map(int, input().split())

result = 0
for i in range(n):
  row = list(map(int, input().split()))
  minNum = min(row)
  
  result = max(result, minNum)

print(result)

