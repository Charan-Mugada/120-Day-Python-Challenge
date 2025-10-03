'''
0 
1 0
0 1 0
1 0 1 0
0 1 0 1 0
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  for j in range(1,i+1):
    print((i+j)%2,end=' ')
  print()