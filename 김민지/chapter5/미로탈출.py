# 19분 49초

from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
  maze.append(list(map(int, input())))

def pathFind(x, y):
  queue = deque()
  queue.append((x, y))

  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  while queue:
    nowX, nowY = queue.popleft()

    for i in range(4):
      nx = nowX+dx[i]
      ny = nowY+dy[i]

      if -1<nx<n and -1<ny<m and maze[nx][ny]==1:
        queue.append((nx, ny))
        maze[nx][ny] = maze[nowX][nowY]+1

  return maze[n-1][m-1]

print(pathFind(0, 0))