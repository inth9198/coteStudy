# 11분 44초

n, m, k = map(int, input().split())    
nums = list(map(int, input().split()))
nums.sort(reverse=True)

firstNum, secondNum = nums[0], nums[1]

divi, remain = m//(k+1), m%(k+1)
# result = (firstNum*((divi*k)+remain)) + (secondNum*divi)
result = (divi*((firstNum*k)+secondNum)) + (remain*firstNum)

print(result)