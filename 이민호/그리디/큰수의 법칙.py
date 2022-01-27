n, m, k = map(int, input().split())
List = list(map(int, input().split()))
List.sort(reverse=True)
result = 0
count = 0
for i in range(m):
    count += 1
    if count > k:
        result += List[1]
        count = 0
    else:
        result += List[0]
print(result)
