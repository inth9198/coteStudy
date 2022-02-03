# 45분 48초

def solution(numbers, target):
  # 전체를 더했을 때 target과 같으면 1 출력
  total = sum(numbers)
  if total==target:
    return 1
  
  # want는 빼야하는 수의 총합 (두 번 더해진거여서 나누기 2) 
  want = (total-target)//2

  # 재귀함수 
  def dfs(numbers, want, idx, cnt):
    for i in range(idx, len(numbers)):
      temp = want
      temp -= numbers[i]

      if temp==0: # 정답 o
        cnt += 1
      elif temp<0: # 정답 x
        continue
      elif temp>0: # 조합 찾기
        cnt = dfs(numbers, temp, i+1, cnt) 

    return cnt

  return dfs(numbers, want, 0, 0)

numbers = [1, 2, 1, 2]
target = 2
print(solution(numbers, target))