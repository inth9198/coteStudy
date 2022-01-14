location = input()
col = int(ord(location[0])) - int(ord('a')) + 1
row = int(location[1])

move = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
cnt = 0

for i in move:
    myLocation_row = row + i[0]
    myLocation_col = col + i[1]
    if 0 < myLocation_col < 9 and 0 < myLocation_row < 9:
        cnt += 1
print(cnt)
