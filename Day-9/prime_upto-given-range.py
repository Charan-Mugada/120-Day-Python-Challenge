n=int(input("Enter the number upto which you want to print prime: "))
prime=[]
for n in range(1,n+1):
  count=0
  for i in range(1,n+1):
    if n%i==0:
      count+=1
  if count==2:
    prime.append(n)
print(prime)
