'''
1   3   5
  2   4
'''
n=int(input("Enter: "))
for i in range(1,n+1,2):
  print(i,end=' ')
print()
for j in range(2,n+1,2):
  print(' '*(2-1),end='')
  print(j,end='')