A, B = map(int, input().split())

visited = [[0] * B for _ in range(A)]

x, y, direction = map(int, input().split())
visited[x][y] = 1

miniMap = []
for i in range(A):
    miniMap.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
count = 1
turnTime = 0
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and miniMap[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turnTime = 0
        continue
    else:
        turnTime += 1
    if turnTime == 4:
        nx = x - dx[direction]
        ny = y + dy[direction]
        if miniMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turnTime = 0
print(count)




'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''