def valid(s):
  if len(s)%2!=0:
    return False
  stack=[]
  for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
      stack.append(s[i])
    else:
      if not stack:
        return False
      check=stack.pop()
      if s[i]==')' and check!='(':
        return False
      if s[i]==']' and check!='[':
        return False
      if s[i]=='}' and check!='{':
        return False
  return not stack 

s=input("Enter: ")
if valid(s):
  print('valid parentheses')
else:
  print('not valid')
