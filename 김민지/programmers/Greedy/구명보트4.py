# 구명보트4.py가 최종 코드입니다!
# 37분 26초

def solution(people, limit):
  people.sort(reverse=True)
  result = 0

  start, end = 0, len(people)-1
  while start<end:
    if people[start]+people[end]<=limit:
      end -= 1

    result += 1
    start += 1

    if start==end:
      result += 1

  return result

print(solution([40, 50, 150, 160], 200))