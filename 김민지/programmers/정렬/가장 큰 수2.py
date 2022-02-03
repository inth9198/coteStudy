# 7, 8, 9, 12, 15 통과

def solution(numbers):
  for i in range(1, len(numbers)):
    for j in range(i, 0, -1):
      a, b = numbers[j-1], numbers[j]

      if a<10 and b>9:
        a *= 10
      elif b<10 and a>9:
        b *= 10

      if a<b:
        numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
      elif a>b:
        break
      elif a==b and numbers[j-1]>numbers[j]:
        numbers[j-1], numbers[j] = numbers[j], numbers[j-1]

  numbers = list(map(str, numbers))
  answer = ''.join(numbers)
  
  return answer


print(solution([3, 30, 34, 5, 9]))