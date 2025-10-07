n=int(input("Enter year: "))
if (n%4==0 and n%100!=0) or (n%400==0):
  print(f"the given year {n} is leap year")
else:
  print(f"the given year is not a leap year")