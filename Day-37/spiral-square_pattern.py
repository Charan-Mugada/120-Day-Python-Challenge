''' 
 1  2  3  4  5
22 23 24 25  6
21 20 19 18  7
14 15 16 17  8
13 12 11 10  9
'''
n=int(input("Enter: "))
mat=[[0 for _ in range(n)] for _ in range(n)]
count=0
for i in range(n):
  for j in range(n):
    if i==0 or j==n-1:
      count+=1
      mat[i][j]=count
for i in range(n-1,0,-1):
  for j in range(n-1):
    if i%2==0:
      if j==0:
        count=count+(n-1)
      mat[i][j]=count
      count-=1
    else:
      if j==0:
        count+=(n-1)
      count+=1
      mat[i][j]=count


    
width = len(str(n*n))
for row in mat:
    print(" ".join(f"{num:>{width}}" for num in row))
