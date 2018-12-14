# ARITHMETIC OPERATORS

# Addition +
# Subtraction -
# Multiplication *
# Division /
# Mod %
# Exponentiation **
# // Divides and rounds down to the nearest integer
# Wait: ^ does not do Exponentiation operation, as in other languages
# - This is used in BitwiseOperators: https://wiki.python.org/moin/BitwiseOperators

# Python holds the usual order of mathematical operations. If you need remember, then click here: http://mathforum.org/dr.math/faq/faq.order.operations.html
# Basic operations: https://www.w3schools.com/python/python_operators.asp

# Below, will print 11
print(4 + 5 + 6 / 3)

# Below, will print 6
print((4 + 6 + 8) / 3)

#VARIABLES
#1. In your variable names, only use ordinary letters, numbers and underscores. They can not have spaces, and need to start with a letter or underscore.
#2. You can not use reserved words or built-in identifiers that have important purposes in Python. Look this: https://docs.python.org/2.5/ref/keywords.html
#3. Use the Snake Case, connecting the words with underscores
an_example_of_variable = "Snake Case connect the words with underscores"

x = 15
y = 4

# Output: x + y = 19
print('x + y = ',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)

# equivalent to x = x + 2
x+=2
# Output: 17
print('x =',x)

#reference: https://www.programiz.com/python-programming/operators