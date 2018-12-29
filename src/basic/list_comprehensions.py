names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name[:name.find(" ")].lower() for name in names] # write your list comprehension here
#for name in names:
#    first_names.append(name[:name.find(" ")])
print(first_names)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [player for player, score in scores.items() if score > 64]
print(passed)