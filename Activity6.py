# Step 2: Import math module
import math

# Step 3: Read values of x1, y1, x2, and y2
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Step 4: Calculate distance using the Pythagorus theorem
d = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

# Step 5: Print the distance
print("Distance between the points:",d )