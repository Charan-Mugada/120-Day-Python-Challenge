'''
we can only climb by 1 step or 2 steps to reach n(its fibo pattern)
'''
def climb(n):
  if n==1:
    return 1
  if n==2:
    return 2
  a,b=1,2
  for i in range(3,n+1):
    a,b=b,a+b
  return b

n=int(input("Enter total no.of steps: "))
print(climb(n))