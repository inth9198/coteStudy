# 29분 24초

n, m = map(int, input().split())
y, x, d = map(int, input().split())
gameMap = []

for i in range(n):
  gameMap.append(list(map(int, input().split())))

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
backMoves = [[1, 0], [0, -1], [-1, 0], [0, 1]]

result = 0
cnt = 0
while True:
  # 네 방향 모두 갈 수 없는 경우 
  cnt += 1
  if cnt>4:
    #뒤로 이동
    gameMap[x][y] = 2
    x, y = x+backMoves[d][0], y+backMoves[d][1]
    cnt = 0

    # 뒤로 이동 시, 바다일 경우
    if gameMap[x][y] == 1:
      print(result)
      break
      
    continue
  
  # 방향 전환
  d -= 1
  if d == -1:
    d = 3

  # 이동할 수 있는 곳 찾기
  nx, ny = x+moves[d][0], y+moves[d][1]
  if -1<nx<n and -1<ny<m and gameMap[nx][ny] == 0:
    gameMap[x][y] = 2
    x, y = nx, ny
    result += 1
    cnt = 0
  

  


  