import seminar
from pprint import pprint

# Let's combine the previous map and filters that we tried earlier
# From seminar.lst, get a list of all the numbers that are divisible by 3, and then
# square them

[x**2 for x in seminar.lst if not x % 3]


# Let's do something a little more interesting. We have some software log in seminar.log
seminar.lprint(seminar.log)
len(seminal.log)

# Pretty big, right? But there's a lot of items with severity level INFO, we want to to
# see only items that are *not* INFO, so:
lst = [event for event in seminar.log if event.severity != 'INFO']
pprint(lst)

# Or maybe we just want to see the content of the events that were caused by client side
# code:
lst = [event.content for event in seminar.log if 'client' in event.location]
pprint(lst)

# Python has other comprehensions, for example, instead of list we can create generators
# Generators are iterables that don't generate the next value until it's been asked for
# It makes them great for chaining togeher or to save memory - a good example is when you
# want to manipulate a huge database result and write the output to a file. You can try
# to generate a list and then save it in one go, but you might require more RAM than you
# should. Instead you can create a generator that performs the manipulation on the db
# cursor and write the lines one by one from the generator
gen1 = (event for event in seminar.log if event.severity != 'INFO')
gen2 = (event.content for event in gen1 if 'client' in event.location)

for event in gen2:
    print event

# You should be careful with generators. Once they ran, they're empty:
for event in gen2:
    print event

# Another type of comprehension is dictionary comprehension. Let's take a look at this
# list of IDs and names
seminar.ids_and_names

# It looks like something that might have come out of a file, let's say we want to
# convert it into a dictionary where the keys are the IDS and the values are the names
{ pair[0:8] : pair[9:] for pair in seminar.ids_and_names }

# Of course we can also run filters. For example let's say we only want IDs that start
# with a digit
{ pair[0:8] : pair[9:] for pair in seminar.ids_and_names if pair[0].isdigit() }


# The last type of comprehension is set comprehension. It's written exactly like
# dictionary comprehension but without the colon, so only the value, but this is left
# as an exercise


# Solution for exercise
{ event.severity for event in seminar.log }
