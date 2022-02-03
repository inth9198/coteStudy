# 11, 16 제외 성공

def solution(citations):
  citations.sort(reverse=True)

  for h in range(len(citations), -1, -1):
    cnt = 0
    for cita in citations:
      if cita>=h:
        cnt += 1
    
    if cnt==h:
      return cnt

print(solution([33, 66]))