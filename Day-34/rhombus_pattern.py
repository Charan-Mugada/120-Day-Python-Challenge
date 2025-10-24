'''
    *****
   *****
  *****
 *****
*****
    *****
   *   *
  *   *
 *   *
*****
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i),end='')
  print('*'*(n))
for i in range(1,n+1):
  print(' '*(n-i),end='')
  for j in range(1,n+1):
    if i==1 or j==1 or i==n or j==n:
      print('*',end='')
    else:
      print(' ',end='')
  print()