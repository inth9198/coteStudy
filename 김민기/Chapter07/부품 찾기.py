# def solution(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid -1
#         else:
#             start = mid + 1
#     return None
#
# n = int(input())
# array = list(map(int, input().split()))
# array.sort()
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     result = solution(array, i, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
#
# # ------------------------------------------
#
# n = int(input())
# array = [0] * 1000001
#
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
#
# ------------------------------------------------

n = int(input())
parts = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if i in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')
















