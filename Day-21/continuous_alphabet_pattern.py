'''
A B C D E F G H I J
K L M N O P Q R S T
U V W X Y Z A B C D
E F G H I J K L M N
O P Q R S T U V W X
Y Z A B C D E F G H
I J K L M N O P Q R
S T U V W X Y Z A B
C D E F G H I J K L
M N O P Q R S T U V
'''
n=int(input("Enter"))
count=65
for i in range(n):
  for j in range(n):
    print(chr(count),end=' ')
    count+=1
    if count>90:
      count=65
  print()
