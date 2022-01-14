N = input()     #정사각형 한 변의 길이
direction=list(input().split())  #방향을 받아 리스트에 넣기
x, y = 1, 1    #현재 좌표

for i in direction:
    if i=='R':
        if y==N: continue
        else: y=y+1
    elif i=='L':
        if y==1: continue
        else: y=y-1
    elif i=='U':
        if x==1: continue
        else: x=x-1
    elif i=='D':
        if x==5: continue
        else: x=x+1
    else:  break

print('(',x,',',y,')')

