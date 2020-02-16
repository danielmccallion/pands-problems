# This program calulates how many tiles you will need
# when tiling a wall or floor (in m2)

length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width

area_needed = area * 1.05

print("You need", area_needed, "tiles in meters squared.")