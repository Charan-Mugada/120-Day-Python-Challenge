def longest_common_prefix(li):
  if not li:
    return ""
  prefix=li[0]
  for s in li[1:]:
    while not s.startswith(prefix):
      prefix=prefix[:-1]
      if prefix=="":
        return ""
  return prefix

li=input().split()
print(longest_common_prefix(li))