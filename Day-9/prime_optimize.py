n=int(input("Enter: "))
flag=0
if n<=1:
  print('Not prime')
else:
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      flag=1
  if flag:
    print('Not prime')
  else:
    print('Prime')
