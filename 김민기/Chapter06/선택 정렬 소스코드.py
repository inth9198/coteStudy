# 선택 정렬
# -	가장 작은 숫자를 차례대로 탐색, 가장 왼쪽 자리부터 스왑
# -	가장 작은 숫자를 선택하는 방식으로 정렬을 진행하여 선택정렬 이라 불림
# 정리
# -	제일 작은 숫자를 찾기 위해 순차적으로 이동
# -	Outer 루프가 한번 돌 때마다 element 하나의 최종 위치가 확정
# -	탐색범위
# 	> Outer : 0 ~ n – 1
# 	    첫 번째 element를 가장 낮은 숫자로 가정하고 시작
#   > Inner : i + 1 ~ n
#       이미 정렬 되어 있는 부분 제외
#       가장 낮은 숫자 다음 인덱스부터 비교하여 스왑
# -	Time Complexity
# 	Worst : O(n^2)
# 	Average : O(n^2)
# 	Best : O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]

print(array)