def solution(name):
    name = list(name)
    answer = 0
    idx = 0
    while 1:
        left, right = 1, 1
        if name[idx] != 'A':
            # 알파벳 바꾸기
            answer += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)
            name[idx] = 'A'

            # 위치 바꾸기
            if name == ['A'] * len(name):
                break
            else:
                for k in range(1, len(name)):
                    if name[idx + k] == 'A':
                        right += 1
                    else:
                        break
                    if name[idx - k] == 'A':
                        left += 1
                    else:
                        break
                if right > left:
                    answer += left
                    idx -= left
                else:
                    answer += right
                    idx += right
    return answer


print(solution('JAZ'))
