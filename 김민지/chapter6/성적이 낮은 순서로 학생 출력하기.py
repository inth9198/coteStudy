# 8분 11초

n = int(input())
stus = {}
for i in range(n):
  key, value = input().split()
  stus[key] = value

stus = sorted(stus.items(), key=lambda item:item[1])

for i in range(n):
  print(stus[i][0], end=" ")