n = int(input())
arr = list(map(int, input().split()))

# dp 테이블 ( 얻을 수 있는 식량의 최댓값을 저장 )
dp = [0] * (n + 1)

dp[0] = arr[0]
# 첫 번째 칸을 털지, 두 번째 칸을 털지 비교
dp[1] = max(arr[0], arr[1])
for i in range(2, n):
    # i - 1 번째 칸까지 털지, i - 2 번째 칸과 i 번째 칸까지 털지 비교
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(dp[n - 1])

