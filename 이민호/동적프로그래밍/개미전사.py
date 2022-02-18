n = int(input())
food = list(map(int, input().split()))
d = [0] * 101
 
d[0] = food[0]
d[1] = max(food[0], food[1])
 
for i in range(2, n):    
    d[i] = max(food[i] + d[i - 2], d[i - 1])
 
print(d[n - 1])
