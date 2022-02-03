def solution(citiations):
    answer = 0
    citiations.sort()
    for i in range(len(citiations)):
        h_index = len(citiations) - i
        if citiations[i] >= h_index:
            answer = h_index
            break
    return answer

print(solution([3, 0, 6, 1, 5]))