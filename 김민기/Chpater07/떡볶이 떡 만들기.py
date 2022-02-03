n, m = map(int, input().split())
noodle = list(map(int, input().split()))

start = 0
end = max(noodle)
while (start <= end):
    sum = 0
    mid = (start + end) // 2
    for i in noodle:
        if i > mid:
            sum += i - mid

    if sum == m:
        break
    elif sum > m:
        start = mid + 1
    else:
        end = mid - 1

print(mid)

