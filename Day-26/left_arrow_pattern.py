'''
    *
   *
  *
 *
*
 *
  *
   *
    *
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i),end='')
  print('*')
for i in range(1,n):
  print(' '*i,end='')
  print('*')
