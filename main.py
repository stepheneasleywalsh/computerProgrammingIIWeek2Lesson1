import math
def rootfactorial(x):
    if not type(x) == int:
        raise TypeError("input is not an integer")
    if x < 0 or x > 20:
        raise ValueError("input must be between 0 and 20 inclusive")
    return(math.sqrt(math.factorial(x)))

# Test it
#print(rootfactorial(-1))
#print(rootfactorial(1.0))
#print(rootfactorial(21))
#print(rootfactorial(10))