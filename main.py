import math

def rootfactorial(x):

    try:
        x = int(input("Give me an integer: "))
    except:
        raise TypeError("ERROR, that is not a valid integer input.")

    try:
        x > 0
    except:
        raise ValueError("ERROR, that is not a positive number.")

    if x < 20:
        x = math.factorial(x)
        return x
    else:
        raise ValueError("ERROR, your input is more than 20.")

    result = math.sqrt(rootfactorial(x))
    return result

    print(result)

quit()