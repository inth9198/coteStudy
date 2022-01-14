#첫째줄 N,M,K의 자연수를 공백으로 구분
N,M,K = map(int, input().split())

#N개의 자연수 입력 -> 공백으로 구분
data = list(map(int,input().split()))

data.sort()  #입력받은 수들을 정렬(오름차순)
first = data[N-1]
second = data[N-2]

result = 0

#무한루프
while True:
    for i in range(K):
        if M==0: break
        result += first
        M -= 1
    if M==0: break

    result += second
    M-=1

print(result)


