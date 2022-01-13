N, M = map(int, input().split())

result = 0
for i in range(N):
    arr = list(map(int, input().split()))
    min_Value = min(arr)
    result = max(result, min_Value)

print(result)