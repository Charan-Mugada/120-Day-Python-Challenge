def is_prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True


upper=int(input('Enter the upper limit: '))
for n in range(2,upper-1):
  if is_prime(n) and is_prime(n+2):
    print(f"({n},{n+2})") 