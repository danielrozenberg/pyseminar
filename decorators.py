# Let's do an example of caching, we'll write our caching function to add a dictionary to
# act as our cache to the function itself. We're only going to support args, not kwargs
# because the version that supports kwargs takes more effort than is worth showing here
def cache(func):
    func.__cache__ = {}
    
    def inner_func(*args):
        if args not in func.__cache__:
            func.__cache__[args] = func(*args)
        return func.__cache__[args]
    return inner_func

# Now let's apply it to a needlessly slow version of Fibonacci
@cache
def slow_fibonacci(n):
    if n in (0, 1):
       return n
    
    for x in xrange(0, 10000000):
        pass
    
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)


# Now let's run it. The first run took a few seconds
slow_fibonacci(10)

# The second run is immediate
slow_fibonacci(10)

# Now let's run it on a bigger number. Slow...
slow_fibonacci(50)

# And fast
slow_fibonacci(50)

# Not that because slow_fibonacci calls itself recursively, all the numbers up to 50 are
# also cached
slow_fibonacci(35)

###
### SWITCH TO SLIDES
###


# Let's write a decorator that sends an email when a function is called
def email(address):
    def decorator(func):
        def inner_func(*args, **kwargs):
            result = func(*args, **kwargs)
            # FIXME send an email with result to address
            print "[Sent an email to %s]" % address
            return result
        return inner_func
    return decorator

# Now let's see, email is:
email

# email with an address is:
email("rodaniel@cs.ubc.ca")

# and a function decorated with the email is:
@email("rodaniel@cs.ubc.ca")
def illegal_access_detected(user, location):
    print "Illegal access detected. User %s attempted to access %s!" % (user, location)
    return 403

illegal_access_detected

# And when we run it it'll "send" the email
illegal_access_detected("Nodir", "NSS Lab")




# Solution to exercise
def throttle(max):
    def decorator(func):
        func.__throttle__ = 0
        
        def inner_func(*args, **kwargs):
            if func.__throttle__ < max:
                func.__throttle__ += 1
                return func(*args, **kwargs)
            print "DANGER!"
        return inner_func
    return decorator


@throttle(2)
def beetlejuice():
    print "Beetlejuice!"

beetlejuice()
beetlejuice()
beetlejuice()
