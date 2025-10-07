'''
E
ED
EDC
EDCB
EDCBA
'''
n=int(input("Enter: "))
for i in range(n,0,-1):
  for j in range(n,i-1,-1):
    print(chr(65+j-1),end='')
  print()