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

#string modulo operator %
print("X: %4d ,Z: %17s, Y: %7.2f " % (x,z,y) )

# Use the 'format' string method to print the same thing
print("X: {0:4d}, Z: {1:17s}, Y: {2:7.2f}".format(10, "I like turtles", 2.24552))

#formatted literals strings
# Finally, print the same thing using an f-string
print(f"X:{x},Y:{y},Z:{z}")