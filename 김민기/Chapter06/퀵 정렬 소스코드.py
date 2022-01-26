# 퀵 정렬
# -	분할정복 알고리즘
# -	피봇을 정한 뒤 피봇의 위치를 확정해가며 정렬
# 정리
# -	분할정복과 정복과정으로 나누어짐
# -	피봇을 정한 뒤 왼쪽 퀵소트, 오른쪽 퀵소트
# -	다양한 피봇 선정 방식 -> 다양한 퀵소트
# -	Time Complexity
#       Worst : O(n^2)
#       Average : O(n log n)
#       Best : O(n log n)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start #피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

#--------------------------------------------------------------------------------

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(arr):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 받음
    return quickSort(left_side) + [pivot] + quickSort(right_side)

print(quickSort(arr))
