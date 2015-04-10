import seminar

# We want more interesting things to reduce, for example let's take a look at this var
seminar.list_of_sets


# set objects have an intersection method that takes two sets, what if we wanted to find
# the intersection of the three sets in the list above, or of any arbitrary list of sets?
reduce(set.intersection, seminar.list_of_sets)



# Solution to exercise:
my_tuple = (False, True, True, False, True)
func = lambda x, y: x + ('1' if y else '0')
reduce(func, my_tuple, '')
