# 1시간 2분 46초

def solution(numbers):
  if sum(numbers) == 0:
    return '0'

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

print(solution([0, 0, 0]))