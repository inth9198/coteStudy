#큐: 선입선출구조(first in first out / 들어온 순서대로 나가게 됨)
#파이썬으로 큐를 구현할 때, collections 모듈에서 제공하는 deque 자료구조 활용

from collections import deque   
queue = deque()

#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)       #먼저 들어온 순서대로 출력  :  deque([3,7,1,4])
queue.reserve()    #역순으로 바꾸기
print(queue)       #나중에 들어온 원소부터 출력 : deque([4,1,7,3])




