from collections import deque
n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))
go=[(1, 0),(0, 1),(-1, 0),(0, -1)]
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    while(Q):
        x, y = Q.popleft()
        for i in range(4):
            nextX = go[i][0] + x
            nextY = go[i][1] + y
            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                continue
            if miro[nextX][nextY] == 0:
                continue
            elif miro[nextX][nextY] == 1:
                miro[nextX][nextY] = miro[x][y] + 1
                Q.append((nextX, nextY))

    return (miro[n-1][m-1])
print(bfs(0,0))
