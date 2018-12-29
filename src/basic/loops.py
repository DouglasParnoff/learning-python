# Python has 2 kinds: for and while
print("--- For loop ---")
# Write a for loop that iterates over the names list to create a userlogin list. 
# To create a userlogin for each name, make everything lowercase and replace
# spaces with underscores. Running your for loop over the list:
names = ["Tomas Delong", "Mark Hoppus", "Travis Barker"]
userlogin = []

# write your for loop here
for name in names:
    userlogin.append(name.replace(" ", "_").lower())
print("-> 1: ")
print(userlogin)

# counting just XML tag
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for item in tokens:
    if item.startswith("<") and item.endswith(">"):
        count += 1
print("-> 2: ")        
print(count)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"
print("-> 3: ")
print(html_str)

# iterating in a dictionary
print("-> 4")
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("-> 5")
#Iterating through keys and values:
for key, value in cast.items():
    print("Actor: {} - Role: {}".format(key, value))
# items is a built-in method  that you can use to iterate over dictionaries in for loops. 
# this method returns tuples of key and value pairs

# while loop
print("-> 6")
item_prices = [1,2,3,4,5,6,7,8,9,10]
max_total = []
while sum(max_total) < 20:
    item = item_prices.pop()
    print("adding item {}".format(item))
    max_total.append(item_prices.pop())

print("max_total: {}".format(sum(max_total)))