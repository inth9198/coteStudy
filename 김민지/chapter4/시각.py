#17분 24초

n = int(input())

#분, 초에서 3이 나오는 경우의 수 : 15개 (3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53)
result = 0
for i in range(n+1):
  if "3" in str(i):
    result += (60*60)
  else:
    result += ((15*60)+(45*15))

print(result)