print("--- ZIP ---")
print("zip 1")
#declaring a lists
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for point in zip(labels, x_coord, y_coord, z_coord):
#    points.append("{}: {}, {}, {}".format(*point))    
    points.append(point)    
    
print("Points:")
for point in points:
    print(point)
    
squares = [x**2 if x % 2 == 0 else x + 1 for x in range(9)]
print(squares)    
print("--- range ---")
for x in range(1, 21):
    print x
    
    
