li=list(map(int,input("Enter: ").split()))
maxii=li[0]
for i in li:
  if i>maxii:
    maxii=i
print(maxii)