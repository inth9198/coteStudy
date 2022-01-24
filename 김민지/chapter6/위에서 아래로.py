# 3분 52초

n = int(input())
nums = []
for i in range(n):
  nums.append(int(input()))

nums.sort(reverse=True)

for i in range(n):
  print(nums[i], end=' ')