def solution(people, limit):
  result = 0

  complete = []
  for i in range(len(people)-1):
    for j in range(i+1, len(people)):
      if people[i]+people[j]<=limit and i not in complete and j not in complete:
        result += 1
        complete.append(i)
        complete.append(j)
        break
  
  result += len(people)-len(complete)

  return result

print(solution([50, 50, 50, 50, 50], 100))