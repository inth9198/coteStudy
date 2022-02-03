# 7분 4초

n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

height = max(ddeok)-1

for h in range(height, -1, -1):
  result = 0
  for i in range(n):
    if ddeok[i]>h:
      result += ddeok[i]-h
  
  if m==result:
    print(h)
    break