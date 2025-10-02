a=int(input("Enter first number: "))
b=int(input("Enter the second number: "))
multi=a*b
while(b!=0):
  r=a%b
  a=b
  b=r
lcm=multi//a
print(lcm)
