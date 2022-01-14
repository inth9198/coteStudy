#현재 위치를 문자열로 받기
loc = input()

y=int(loc[1])
x=int(ord(loc[0]))-int(ord('a'))+1     #loc[0]='a'인경우 1 -> 1='a'

cnt=0
plan=[(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(1,-2),(-1,-2),(-1,2)]

for i in plan:
    dx = i[0] + x
    dy = i[1] + y

    if dx >=1 and dx <= 8 and dy >= 1 and dy<=8:
        cnt+=1

print(cnt)
