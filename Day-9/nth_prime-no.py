n=int(input("Enter the position: "))
result=[]
for i in range(1,n**2):
  count=0
  for j in range(1,n**2):
    if i%j==0:
      count+=1
  if count==2:
    result.append(i)
print(result[n-1])
