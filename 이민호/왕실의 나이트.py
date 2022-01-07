spot = input()
result = 0
now = [int(ord(spot[0])) - int(ord('a')) + 1, int(spot[1])]
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-1, 2), (-2, 1), (2, 1), (1, 2)]
for i in steps:
    now[0] += i[0]
    now[1] += i[1]
    if 8 >= now[0] and  1 >= now[0]  and 8 >= now[1] and now[1] >= 1:
        result += 1
    now = [int(ord(spot[0])) - int(ord('a')) + 1, int(spot[1])]
print(result)