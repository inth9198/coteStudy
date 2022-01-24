def quickSort(array, start, end):
  if start >= end:
    return

  pivot = start
  left, right = start+1, end

  while left<=right:
    while left<=end and array[left]<=array[pivot]:
      left += 1

    while start<right and array[pivot]<=array[right]:
      right -= 1

    if left>right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]

  quickSort(array, start, right-1)
  quickSort(array, right+1, end)  

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quickSort(array, 0, len(array)-1)

print(array)
