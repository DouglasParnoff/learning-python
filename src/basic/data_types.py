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