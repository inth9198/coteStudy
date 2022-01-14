from itertools import combinations

def solution(people, limit):
  coms = list(combinations(people, 2))

  result = 0
  for com in coms:
    if sum(com)<=limit and com[0] in people and com[1] in people:
      result += 1
      people.remove(com[0])
      people.remove(com[1])

  result += len(people)

  return result

print(solution([70, 50, 80], 3))