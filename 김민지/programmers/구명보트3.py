# 정확성 테스트 통과 / 효율성 테스트 통과X

def solution(people, limit):
  people.sort()
  result = 0

  complete = []
  for i in range(len(people)-1):
    for j in range(len(people)-1, i, -1):
      if people[i]+people[j]<=limit and i not in complete and j not in complete:
        result += 1
        complete.append(i)
        complete.append(j)
        break
  
  result += len(people)-len(complete)

  return result

print(solution([40, 50, 150, 160], 200))