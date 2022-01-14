#재귀함수를 이용하여 n! 구현하기
def factorial_recursive(n):
  if n<=1:       #1일때 1을 반환하고 끝
    return 1
  
 return n*factorial_recursive(n-1)

print(factorial_recursive(5))
