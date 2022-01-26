n = int(input())
arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

array = sorted(arr, key=lambda arr: arr[1])

print(arr)
for student in arr:
    print(student[0], end=' ')