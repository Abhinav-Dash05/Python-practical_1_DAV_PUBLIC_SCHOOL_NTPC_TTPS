import math

# Given values
a = int(input("Enter perpendicular side: "))  # One side
b = int(input("Enter base side: "))  # Another side
angle_deg = int(input("Enter angle between perpendicular and base side: "))  # Angle in degrees

# Convert angle to radians
angle_rad = math.radians(angle_deg)

# Calculate the third side
# Using Pythagorean theorem for right-angled triangle
c = math.sqrt(a**2 + b**2) if angle_deg == 90 else (
    a / math.cos(angle_rad) if a else (
        b / math.sin(angle_rad) if b else (
            math.sqrt(a**2 + b**2)
        )
    )
)

print(f"The third side of the triangle is: {c}")