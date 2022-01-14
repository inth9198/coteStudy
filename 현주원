M,N = map(int,input().split())    # M:열 / N:행
max_data = 0

for i in range(N):
    data = list(map(int,input().split()))

    #방금 입력한 줄에서 가장 작은 값 찾기
    min_data = 10001    #각 숫자가 1부터 10000
    for a in data:
        min_data = min(min_data,a)   #min_data = min(data)

    #작은 값들 중 큰 값 고르기
    max_data = max(max_data,min_data)

print(max_data)
