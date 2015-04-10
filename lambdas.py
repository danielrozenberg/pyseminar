# Define a simple function
def f(x, y):
    return x**2 + y**2

# Use function, show what "f" is
f(6, 7)
f
type(f)
f.func_name

# Redefine that function with the lambda syntax
# Notice the lack of "return". A lambda function returns the expression's value
f = lambda x, y: x**2 + y**2

# Use the lambda function, show what "f" is
f(6, 7)
f
type(f)
f.func_name


# We can use lambda expressions to create function generators, or on-the-fly functions
def make_inc(n):
    return lambda x: x + n

# The make_inc function returns a new functions, that function increases the parameter by n
# n is a constant in this lambda function, x is a paramter

inc_1 = make_inc(1)
inc_5 = make_inc(5)

inc_1(10)
inc_5(10)

# Of course, we can chain the function calls
# in this case we call make_inc with n=3 and then call the resulting function with x=4
make_inc(3)(4)

# We can deine make_inc using nested lambdas!
# But don't do it, it's ugly and less readable :)
make_inc = lambda n: lambda x: x + n


# Solution to exercise:
def make_matrix(n, m):
    return lambda x: [[x] * m] * n

