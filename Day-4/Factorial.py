n=int(input("Enter: "))
fact=1
for i in range(n,1,-1):
  fact*=i

print('The factorial of the given number is:',fact)