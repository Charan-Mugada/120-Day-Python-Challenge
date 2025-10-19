li=list(map(int,input("Enter: ").split()))
seen=[]
for ele in  li:
  if ele not in seen:
    seen.append(ele)
print(seen)