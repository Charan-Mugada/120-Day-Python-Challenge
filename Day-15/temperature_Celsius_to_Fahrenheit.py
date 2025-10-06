option=int(input("Press 1 to change temp from fahrenheit to celsius:\nPress 2 to change temp from celsius to fahrenheit:"))
if option==1:
  f=int(input("Enter temperature:"))
  c=((5/9)*(f-32))
  print(f"The temperature in celsius format is {c:.2f}")
else:
  c=int(input("Enter temperature:"))
  f=((9/5)*c+32)
  print(f"The temperature in fahrenheit format is {c:.2f}")