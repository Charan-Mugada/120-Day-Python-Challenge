li=list(map(int,input("Enter list of elements: ").split()))
target=int(input("Enter target: "))
for i in range(len(li)):
  for j in range(i+1,len(li)):
    if li[i]+li[j]==target:
      print([i,j])
      found = True
      break
  if found:
      break

if not found:
    print("No pair found")