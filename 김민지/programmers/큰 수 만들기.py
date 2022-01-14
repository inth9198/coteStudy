# 2시간 43분

def solution(number, k):
  sortNum = ''.join(sorted(number, reverse=True))
  if sortNum == number:
    return number[:len(number)-k]
  
  result = []
  for num in number:
    while k>0 and result and result[-1]<num:
      result.pop()
      k -= 1

    result.append(num)
    
  return ''.join(result)

print(solution("9999999999", 5))