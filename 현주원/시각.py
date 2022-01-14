#Q: 정수 N을 입력받고, 00시 00분 00초 ~ N시 59분 59초 사이에서 3이 나온 경우의 수 구하기

#N을 입력받기
N= int(input())

h, m, s, cnt = 0,0,0,0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)


#str -> 계산결과와 문자열을 연결할 때 사용


