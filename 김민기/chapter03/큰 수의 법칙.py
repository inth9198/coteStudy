N, M, K = map(int, input().split()) # N : 배열의 크기, M : 더해지는 횟수, K : 연속될 수 있는 횟수
arr = list(map(int, input().split()))
sum = 0
cnt = 0

arr.sort(reverse=True)

while cnt < 8:
    idx = 0
    for i in range(K):  # 가장 큰 수 sum에 K번 누적
        sum += arr[idx]
        cnt += 1        # 누적 한 횟수 증가
    idx += 1            # 두 번째로 큰 수 sum에 1번 누적
    sum += arr[idx]     # 누적 한 횟수 증가
    cnt += 1

print(sum)