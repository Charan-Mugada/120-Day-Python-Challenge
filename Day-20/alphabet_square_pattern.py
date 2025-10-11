'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
n=int(input("Enter: "))
for i in range(n):
  for j in range(n):
    print(chr(65+j),end=' ')
  print()