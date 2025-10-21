'''
     *
    ***
   *****
  *******
 *********
***********
    ***
    ***
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i),end='')
  print('*'*(2*i-1))
for i in range(2):
  print(' '*((n//2)+1),end='')
  print('*'*(n//2))
