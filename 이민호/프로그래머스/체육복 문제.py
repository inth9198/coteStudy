def solution(n, lost, reserve):
    std = []
    answer = 0
    #0번 학생은 없습니다.
    for i in range(n+1):
        std.append(1)
    for i in lost:
        std[i] = 0
    lost.sort() #정렬을 꼭 해야 합니다 정렬되지 않은 테케가 들어오기도 합니다
    reserve.sort()#
    for i in reserve:  #후에 친구가 먼저 자기껄 빌려줄수가 있습니다.
        if std[i] == 0:
            std[i] = 1
        elif i >= 2 and std[i - 1] == 0:
            std[i - 1] = 1
        elif i <= n - 1 and std[i + 1] == 0:
            if (i + 1 in reserve):
                continue
            std[i + 1] = 1
    for i in range(1, n + 1):
        if std[i] == 1:
            answer += 1
    return answer
