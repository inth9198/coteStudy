# 다 틀림

def solution(citations):
  citations.sort()
  hIndex = []

  for i in range(len(citations)):
    hIndex.append(len(citations[i:]))

  for j in range(len(citations)-1, -1, -1):
    if citations[j]==hIndex[j]:
      return citations[j]

print(solution([33, 36]))