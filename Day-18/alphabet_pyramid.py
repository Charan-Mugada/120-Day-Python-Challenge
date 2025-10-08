'''
   A
  ABA
 ABCBA
ABCDCBA
 ABCBA
  ABA
   A
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i),end='')
  for j in range(1,i+1):
    print(chr(65+j-1),end='')
  for k in range(j-1,0,-1):
    print(chr(65+k-1),end='')
  print()
for i in range(n-1,0,-1):
  print(' '*(n-i),end='')
  for j in range(1,i+1):
    print(chr(65+j-1),end='')
  for k in range(j-1,0,-1):
    print(chr(65+k-1),end='')
  print()
