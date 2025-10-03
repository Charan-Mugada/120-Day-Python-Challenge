'''
1
0 0
1 1 1
0 0 0 0
1 1 1 1 1
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  for j in range(i):
    print((i%2),end=" ")
  print()
