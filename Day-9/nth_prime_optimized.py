def is_prime(n):
  if n==1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

n=int(input("Enter the number upto which you want to print prime: "))
prime=[]
for i in range(1,n+1):
  if is_prime(i):
    prime.append(i)
print(prime)