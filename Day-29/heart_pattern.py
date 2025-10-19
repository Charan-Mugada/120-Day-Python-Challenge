'''
 ***   ***
***** *****
***********
 *********
  *******
   *****
    ***
     *    
'''
n=int(input("Enter: "))
for i in range(n//2, n, 2):  
    print(' ' * ((n - i)//2), end='') 
    print('*' * i, end='')          
    print(' ' * (n - i), end='')         
    print('*' * i)                   

for i in range(n,0,-1):
  print(' '*(n-i),end='')
  print('*'*((i*2)-1))