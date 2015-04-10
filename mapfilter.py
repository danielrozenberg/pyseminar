import seminar

# Let's see what's inside our list "lst"
seminar.lst

# Let's say we want to get a list with all the items squared, we can define a square
# function and then run map:
def square(x):
    return x**2

map(square, seminar.lst)


# Of course, since the first parameter is a function we can just use a lambda expression
map(lambda x: x**2, seminar.lst)


# Filter acts pretty much the same way. Let's say we want to get all the odd numbers
# The truth value of numbers in Python is False for 0, True for everything else, so:
filter(lambda x: x % 2, seminar.lst)



# Solution to exercise:
filter(lambda x: not x % 3, seminar.lst)
