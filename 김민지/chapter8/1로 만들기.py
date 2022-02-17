# 15분 49초

x = int(input())
arr = [0]*(x+1)

stack = [x]
for i in range(1, x):
  newX = stack[0]
  stack = stack[1:]

  if not arr[newX-1]:
    arr[newX-1] = arr[newX]+1
    stack.append(newX-1)

  if newX%2==0 and not arr[newX//2]:
    arr[newX//2] = arr[newX]+1
    stack.append(newX//2)
  
  if newX%3==0 and not arr[newX//3]:
    arr[newX//3] = arr[newX]+1
    stack.append(newX//3)
  
  if newX%5==0 and not arr[newX//5]:
    arr[newX//5] = arr[newX]+1
    stack.append(newX//5)

  if arr[1]!=0:
    print(arr[1])
    break

# x = int(input())
# d = [0]*(x+1)

# for i in range(2, x+1):
#   d[i] = d[i-1]+1

#   if i%2==0:
#     d[i] = min(d[i], d[i//2]+1)
  
#   if i%3==0:
#     d[i] = min(d[i], d[i//3]+1)

#   if i%5==0:
#     d[i] = min(d[i], d[i//5]+1)

# print(d[x])
