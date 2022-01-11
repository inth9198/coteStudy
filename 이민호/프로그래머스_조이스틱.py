def solution(name):
    answer = 0
    move = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        lastA = i + 1
        while lastA < len(name) and name[lastA] == 'A':
            lastA += 1
        move = min(move, i + i + len(name) - lastA)
    answer += move
    return answer
r2= solution("ABAAB")
print(r2)
#GAAArrrAA
#AAAeeA
#eeeAAAAAAAaAAAAAAq
#다 A인경우
