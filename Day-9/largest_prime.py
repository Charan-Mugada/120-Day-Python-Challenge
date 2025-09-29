n=int(input("Enter: "))
while n%2==0:
  largest=2
  n=n//2
for i in range(3,int(n**0.5)+1,2):
  while n%i==0:
    largest=i
    n=n//i

if n>1:
  print(n)
else:
  print(largest)