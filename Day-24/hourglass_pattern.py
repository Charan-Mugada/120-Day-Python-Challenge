'''
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(i-1),end='')
  print('*'*(2*(n-i)+1))
for j in range(n-1,0,-1):
  print(' '*(j-1),end='')
  print('*'*(2*(n-j)+1))