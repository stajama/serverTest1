import bleach

def cleanAndCheckNumber(numberString):
    x = bleach.clean(numberString)
    try:
        x = int(x)
        if x > 100 or x < 1:
            raise ValueError
    except ValueError:
        raise ValueError("Input must be a valid number from 1 to 100.")
    return x

