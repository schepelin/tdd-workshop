

def is_perfect(number):
    factors = []
    factors.append(1)
    factors.append(number)

    i = 2
    while i < number:
        if number % i == 0:
            factors.append(i)
        i += 1

    return sum(factors) - number == number
