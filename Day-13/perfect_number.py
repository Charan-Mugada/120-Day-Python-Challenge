n=int(input("Enter a number to check whether its perfect num or not: "))
orginal=n
sum1=0
for i in range(1,n):
  if n%i==0:
    sum1+=i
if orginal==sum1:
  print("The given number is a perfect number")
else:
  print("The given number is not a perfect number")