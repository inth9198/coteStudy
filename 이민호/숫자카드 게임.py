n, m = map(int, input().split())
for i in range(n):
    listN = list(map(int, input().split()))
    minN = min(listN)
    if i == 0:
        minInMax = minN
    if minInMax < minN:
        minInMax = minN
print(minInMax)
