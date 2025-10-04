'''
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(" "*(n-i),end='')
  for j in range(1,i+1):
    print(j,end='')
  for k in range(i-1,0,-1):
    print(k,end='')
  print()
for i in range(n-1,0,-1):
  print(' '*(n-i),end='')
  for j in range(1,i+1):
    print(j,end='')
  for k in range(j-1,0,-1):
    print(k,end='')
  print()
