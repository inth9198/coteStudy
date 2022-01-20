# 24분 54초

n, m = map(int, input().split())

iceMold = []
for i in range(n):
  iceMold.append(list(map(int, input())))

def iceCnt(x, y):
  if x<0 or x>=n or y<0 or y>=m:
    return False

  if iceMold[x][y]==0:
    iceMold[x][y]=2
    iceCnt(x, y+1) # right
    iceCnt(x, y-1) # left
    iceCnt(x+1, y) # down
    iceCnt(x-1, y) # up

    return True

  return False

result = 0
for i in range(n):
  for j in range(m):
    if iceMold[i][j]==0 and iceCnt(i, j)==True:
      result += 1

print(result)



# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
