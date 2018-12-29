# Integer and Float types
print("--- INT AND FLOAT ---")
x = 2   # x is an integer
y = 3.5 # y is a float
print('x: ', + x)
print('y: ', + y)
print(type(x))
x = float(x)
print(type(x))
# you can see more about float here: https://docs.python.org/3/tutorial/floatingpoint.html

#NEVER do this:
# print(5/0)

# Bool type
print("--- BOOL ---")
bool_variable = x < 1
print(type(bool_variable))
print('bool_variable: ', bool_variable)
print('not(bool_variable): ', not(bool_variable))

# Truth Value
# We can use non-boolean objects in a boolean expression of an if statement (woooww!) 
# Here are most of the built-in objects that are considered False in Python:
# - constants defined to be false: None and False
# - zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# - empty sequences and collections: '"", (), [], {}, set(), range(0)
errors = 6
if errors:
    print("Wait: there are {} errors to fix!".format(errors))
else:
    print("Congratulations: no errors found!")
    
# String type
print("--- STRING ---")
my_string = 'Let\'s go, baby!'
print(type(my_string))
print(my_string)
print(len(my_string))
# doesn't work: print(len(132))
print(my_string[0])
print(my_string[1])
print(my_string[2])