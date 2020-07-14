"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]



# for (i, elem) in enumerate(range(6)):
#     y.append(i+1)

# for x in range(5):
#     y.append(x+1)

y = [i for i in range(1,6)]
print(y)
print()

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



# y = []
# for x in range(10):
#     y.append(x**3)

y = [num**3 for num in range(0,10)]
# y = [num**3 for num in range(10)]
print(y)
print()

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [i.upper() for i in a]

# for x in a:
#     y.append(x.upper())

print(y)
print()

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# Look up more split methods

# What do you need between the square brackets to make it work?
# y = []
# y2= [int()][1:] # To remove '0' from list
# y2= [int()] # Starts all lists with a '0' for some reason
y = [i for i in x if int(i) % 2 == 0]

# for num in x:
#     if int(num) % 2 == 0:
#         y.append(num)
#         y2.append(num)

print(y)
# print(y2) # Why does this start with '0'?
print()