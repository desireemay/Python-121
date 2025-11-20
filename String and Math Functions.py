import math

name = input("Enter your name: ").strip().title()
radius = float(input("Enter radius: "))

area = math.pi * math.exp(2 * math.log(radius))

print(f"Hello {name}, the area is {area:.2f}")
