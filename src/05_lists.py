# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)
print()

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)
print()

# Change x so that it is [1, 2, 3, 4, 9, 10]
# x.remove(8)
del x[4]
print(x)
print()

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)
print()

# Print the length of list x
print(len(x))
print()

# Print all the values in x multiplied by 1000
for n in x:
    print(n * 1000)