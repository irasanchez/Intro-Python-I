"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# learning notes:
#   miss any of the syntax after the '%'s and get this error:
#   ValueError: unsupported format character ','
#   d digit, .2f is to decimals in of float, s is string
print("1. printf operator: ", 'x is %d, y is %.2f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
print("2. 'format' string: ", 'x is {}, y is {:.2f}, z is "{}"')

# Finally, print the same thing using an f-string
print("3. f-string: ", f'x is {x}, y is {y:.2f}, z is "{z}"')