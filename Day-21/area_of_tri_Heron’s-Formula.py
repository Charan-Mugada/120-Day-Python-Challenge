'''when all sides are given'''
import math
a=float(input("Enter: "))
b=float(input("Enter: "))
c=float(input("Enter: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"the area of traingle is {area}")