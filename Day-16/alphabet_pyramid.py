'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''
n=int(input("Enter: "))
for i in range(n):
  print(' '*(n-i-1),end='')
  for j in range(i+1):
    print(chr(65+j),end='')
  for k in range(j,0,-1):
    print(chr(65+(k-1)),end='')
  print()