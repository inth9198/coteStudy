# 7, 8 통과

def solution(numbers):
  answer = ''

  single, double = [], []
  for num in numbers:
    if num<10:
      single.append(num)
    else:
      double.append(num)
  
  single.sort(reverse=True)
  double.sort(reverse=True)

  s, d = 0, 0
  for i in range(len(numbers)):
    if single[s]*10>=double[d]:
      answer += str(single[s])
      s += 1
    else:
      answer += str(double[d])
      d += 1

    if s>=len(single):
      for j in double[d:]:
        answer += str(j)
      break
    elif d>=len(double):
      for j in single[s:]:
        answer += str(j)
      break

  return answer

print(solution([3, 30, 34, 5, 9]))