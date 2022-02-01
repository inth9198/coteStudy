n, m = list(map(int, input().split(' ')))
dduckList = list(map(int, input().split()))
start = 0
end = max(dduckList)
def findLen(arr, mid):
    len = 0
    for i in arr:
        if (i - mid) > 0:
            len += (i - mid)
    return len
while(start <= end):
    mid = (end + start)//2
    len = findLen(dduckList, mid)
    if len < m:
        end = mid - 1
    else :
        answer = mid
        start = mid + 1
print(answer)
