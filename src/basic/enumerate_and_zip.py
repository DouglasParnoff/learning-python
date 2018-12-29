print("--- ZIP ---")
print("zip 1")
#declaring a lists
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# zip all list and put to label, x, y and z variables
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(label, x, y, z))
#for point in zip(labels, x_coord, y_coord, z_coord):
#    points.append("{}: {}, {}, {}".format(*point))    
print("Points:")
for point in points:
    print(point)

print("zip 2")    
#zip list to a dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
#all lists to zip to dictionary
cast = dict(zip(cast_names, cast_heights))
print(cast)

print("zip 3")
#a zip tuple
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names = ()
heights = ()
for name, height in cast:
    names += (name,)
    heights += (height,)

print(names)
print(heights)

print("zip 4")
# tuple of tuple
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# break tuple of tuple, unziping (to a list of tuple) and parsing to tuple
print(zip(*data[:]))
data_transpose = tuple(zip(*data[:]))
print(data_transpose)

print("enumerate 5")

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, person in enumerate(cast):
    cast[i] = "{} {}".format(person, heights[i])

print(cast)