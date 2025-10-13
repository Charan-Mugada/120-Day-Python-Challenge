n=int(input("Enter: "))
length=len(str(n))
x=n
sum1=0
while(x!=0):
  s=x%10
  sum1+=(s**length)
  x=x//10

if sum1==n:
  print('Armstrong number')
else:
  print('Not armstrong number')