x = int(input())
dp = [0] * (x + 1)

for i in range(2, x + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 2와 나누어 떨어질 경우 & 1을 빼는 경우 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3와 나누어 떨어질 경우 & 직전 경우 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 5와 나누어 떨어질 경우 & 직전 경유 비교
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[x])
