'''
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''
n=int(input("Enter: "))
for i in range(n):
  print(' '*i,end='')
  print('* '*(n-i))
for i in range(n-1,0,-1):
  print(' '*(i-1),end='')
  print('* '*(n-i+1))

