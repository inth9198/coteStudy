def solution(N, number):
    dp = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        tmp = []
        patton = int(str(N) * i)
        tmp.append(patton)
        for j in range(1, i//2+1):
            for k in dp[j]:
                for l in dp[i - j]:
                    tmp.append(k+l)
                    tmp.append(k - l)
                    tmp.append(-k + l)
                    tmp.append(k * l)
                    if l != 0:
                        tmp.append(k / l)
                    if k != 0:
                        tmp.append(l / k)
            if number in tmp:
                return i
            dp.append(tmp)
    return -1
