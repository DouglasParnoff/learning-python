#DATA STRUCTURES
print("--- LIST ---")
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(len(days))
print(days[0])
print(days[1]) # [...]
print(days[-1]) # wow! you can use "index by end of the list" with negative index
print(days[-2])
days[1] = 2 # now, the list is a mix of data types
print(days[1]) # [...]
print(days[0:3]) # slice include the lower index and exclude the upper index

print('Monday' in days)
False
print("Doulgas" not in "Hi, my name is Julia")

# Mutability: change the value of object after it has been created
# -> list is and String isn't
# Order: used to access a specific position of object
# -> list and string

print("--- TUPLE ---")
#UNMUTABLE!
#ORDERED
months = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
# or can do like this: months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print("@".join(months))

print("--- SET ---")
#"Set is a data type for mutable unordered collections of unique elements
# Are unordered: there is no "last element"
numbers = [1, 1, 1, 2, 3, 3, 3]
set_of_numbers = set(numbers)
print(set_of_numbers)
# equality VS identity
numbers_b = numbers
numbers_c = [1, 1, 1, 2, 3, 3, 3]
print(numbers == numbers_b)
print(numbers is numbers_b)
print(numbers == numbers_c)
print(numbers is numbers_c)

print("--- DICTIONARY ---")
# A dictionary is a mutable data type that stores mappings of unique keys to values. 
# Here's a dictionary that stores elements and their atomic numbers.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements.get("hydrogen"))
print(elements.get("something"))
print(elements.get("something", "Custom Error: there isn't something"))

def multiply(a, b):
  return a * b
  
print(multiply(3,2))

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

#passed = [player for player in score if score <= 65]
passed = []
for player, score in scores.items():
    if score >= 65:
        passed.append(player)
print(passed)
passed = []
# or can do with a list comprehension
passed = [player for player, score in scores.items() if score > 64]