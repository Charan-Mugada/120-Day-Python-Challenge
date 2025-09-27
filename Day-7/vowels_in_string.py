s=input("Enter: ").lower()
count=0
for i in s:
  if i in 'aeiou':
    count+=1
print(f"Total number of vowels are: {count}")