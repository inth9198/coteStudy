# 3분 43초

def solution(array, commands):
  answer = []
  for start, end, target in commands:
    cutArray = array[start-1:end]
    cutArray.sort()
    answer.append(cutArray[target-1])

  return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))