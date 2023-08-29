import math
a = float(input("Enter value for a "))
b = float(input("Enter value for b "))
c = float(input("Enter Value for c "))
m = b*b - (4*a*c)
print(m)
x1 = (b * math.sqrt(m))/(2 * a)
x2 = ((-b) * math.sqrt(m))/(2 * a)
print(f"x1 = {x1} and x2 = {x2}")