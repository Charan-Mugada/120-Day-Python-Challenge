'''
A
B C
D   E
F     G
H I J K L
'''
n=int(input("Enter: "))
count=0
for i in range(1,n+1):
  for j in range(1,i+1):
    if count>=26:
      count=0
    if i==1 or i==n or j==1 or j==i:
      print(chr(65+count),end=' ')
      count+=1
    else:
      print(' '*(j//2),end=' ')
  print()

