
def is_perfect(number):
    pass
    # initialize factors
    # check if number a factor <--- simpliest thing to do
    # sum factors


class PerfectNumberClassifier:

    def __init__(self, number):
        self._number = number

    def is_factor(self, factor):
        return self._number % factor == 0

    def get_factors(self):
        factors = []
        factors.append(1)

        i = 2
        while i < self._number:
            if self.is_factor(i):
                factors.append(i)
            i += 1

        factors.append(self._number)
        return factors
