# 삽입 정렬
# -	정렬된 어레이를 유지하며 진행
# -	새로운 숫자가 삽입되면 정렬된 어레이 안에서 자기의 자리를 찾아가며 정렬
# 정리
# -	정렬된 partial 어레이를 유지하며 한 칸씩 늘려가며 정렬
# -	한 칸 늘릴 때 새로 삽입된 데이터를 정렬된 어레이에서 맞는 자리로 위치시킨다.
# -	탐색범위
#   >Outer : 1  n
#       정렬된 어레이를 유지할 때 시작 사이즈를 2로 설정
#   >Inner : j >= 0 && arr[j] > key
#       정렬된 어레이를 끝까지 탐색을 안했고
#       현재 값 보다 키(자신의 값)가 더 작으면 > 왼쪽으로 이동
# -	Time Complexity
# 	    Worst : O(n^2)
# 	    Average : O(n^2)
#       est : O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):       # 인덱스 i 부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)