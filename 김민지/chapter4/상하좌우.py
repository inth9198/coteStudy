# 9분 40초

n = int(input())
moves = input().split()

x, y = 1, 1
for i in range(len(moves)):
  if moves[i]=="L" and y>1:
    y -= 1
  elif moves[i] == "R" and y<n:
    y += 1
  elif moves[i] == "U" and x>1:
    x -= 1
  elif moves[i] == "D" and x<n:
    x += 1

print(x, y)