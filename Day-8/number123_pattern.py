'''
1
22
333
4444
'''

n=int(input("Enter: "))
for i in range(n):
  for j in range(i):
    print(i,end='')
  print()