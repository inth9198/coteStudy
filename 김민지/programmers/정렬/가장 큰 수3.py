# 11번 제외하고 다 성공

def solution(numbers):
  numbers = list(map(str, numbers))

  changeNum = []
  idx = 0
  for num in numbers:
    num *= 4
    changeNum.append((num[0:4], idx))
    idx += 1

  changeNum.sort(reverse=True)

  answer = ''
  for _, idx in changeNum:
    answer += numbers[idx] 

  return answer

print(solution([3, 30, 34, 5, 9]))