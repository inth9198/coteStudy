n = int(input())
allCom = list(map(int, input().split()))
m = int(input())
callCom = list(map(int, input().split()))
def biSearch(arr, target, left, right):
    if (right <= left):
        return False
    mid = int((left + right) / 2)
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return biSearch(arr, target, left, mid-1)
    else :
        return biSearch(arr, target, mid + 1, right)

for i in callCom:
    if biSearch(allCom, i, 0, n-1):
        print("yes")
    else :
        print("no")
