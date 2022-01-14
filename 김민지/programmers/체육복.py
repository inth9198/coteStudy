def solution(n, lost, reserve):
  lost.sort()
  reserve.sort()   
  same = set(lost)&set(reserve)

  lost = list(set(lost)-same)
  reserve = list(set(reserve)-same)
  
  for i in range(len(reserve)):
    front, back = reserve[i]-1, reserve[i]+1
    
    if front in lost:
      lost.remove(front)
      continue
    elif back in lost:
      lost.remove(back)
      continue
          
  return n-len(lost)

print(solution(5, [4, 3], [3, 2]))