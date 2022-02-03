# 12분 56초

def binarySearch(array, target, start, end):
  while start<=end:
    mid = (start+end)//2

    if array[mid]==target:
      return print("yes", end=" ")
    elif array[mid]>target:
      end = mid-1
    else:
      start = mid+1

n = int(input())
nArray = list(map(int, input().split()))

m = int(input())
mArray = list(map(int, input().split()))

nArray.sort()

for i in range(m):
  if mArray[i] not in nArray:
    print("no", end=" ")
  else:
    binarySearch(nArray, mArray[i], 0, n-1)
  
