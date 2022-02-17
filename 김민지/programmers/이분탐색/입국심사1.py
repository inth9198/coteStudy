# 1, 2, 3 통과

def solution(n, times):
  arr = []
  for i in range(1, n+1):
    for time in times:
      arr.append(time*i)
  
  arr.sort()

  answer = arr[n-1]

  return answer

print(solution(6, [7, 10]))