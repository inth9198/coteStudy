# 20분 25초

start = input()

columns = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8"}
col, row = int(columns[start[0]]), int(start[1])

moves = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

result = 0
for move in moves:
  if 0<col+move[0]<9 and 0<row+move[1]<9:
    result += 1

print(result)
