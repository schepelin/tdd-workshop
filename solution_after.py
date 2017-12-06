import math


def is_perfect(number):
    factors = []
    factors.append(1)
    factors.append(number)

    i = 2
    while i <= int(math.sqrt(number)):
        if number % i == 0:
            factors.append(i)
            symmetrical_factor = int(number / i)

            # guard condition for numbers e.g. 16
            if symmetrical_factor != i:
                factors.append(symmetrical_factor)
        i += 1

    return sum(factors) - number == number
