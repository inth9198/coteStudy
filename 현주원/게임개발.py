#책참고(다시 풀어보기)

#맵 생성(세로:N/가로:M)
N,M=map(int,(input().split()))

#현재 캐릭터의 위치(A,B)와 바라보고 있는 방향(direction)
A,B,direction=map(int, input().split())

#방문한 좌표 확인하기 위해서 모든 좌표를 0으로 처리
d=[[0]*M for _ in range()]
#현재 좌표를 방문한 좌표로 변경
d[A][B] = 1

#맵 환경 생성(바다 :1/ 육지:0)
array=[]
for i in range(N):
    array.append(list(map(int,input().split())))

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽방향부터 차례대로 갈 곳 정함(반시계방향으로 회전)
def left():
    global direction
    direction -= 1   #왼쪽 방향으로 한 칸 전진
    if direction == -1:       #왼쪽 방향으로 진행하다가 더 이상 갈 곳 없는 경우
        direction = 3      #반시계방향 다음방향인 남쪽

#캐릭터가 방문하는 칸의 갯수 횟수 세기(현재 좌표 추가해줌)
count = 1

while True:
    left()        #왼쪽방향으로1칸이동하는 함수 실행
    nx = A+dx[direction]  #함수실행 후 x좌표
    ny = B+dy[direction]  #함수실행 후 y좌표
    if d[nx][ny]==0 and array[nx][ny]==0 :     #가보지 않고 육지인경우
        d[nx][ny]=1  #방문처리
        A=nx
        A=ny
        count+=1
        turn_time=0
        continue

    #회전 이후 정면에 가보지 않은 칸이 없거나 바다가 있는경우
    else:
        turn_time+=1

    #네 방향 모두 갈 수 없는 경우(방향을 유지한 채 한 칸 뒤로)
    if turn_time==4:
        nx = A-dx[direction]
        ny = B-dy[direction]
            
        if array[nx][ny]==0:   #육지인경우
            x=nx
            y=ny
                
        else:
            break
        turn_time=0
            
print(count)
                






