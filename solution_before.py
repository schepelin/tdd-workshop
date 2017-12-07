
def is_perfect(number):
    pass
    # initialize factors
    # check if number a factor <--- simpliest thing to do
    # sum factors


class PerfectNumberClassifier:

    def __init__(self, number):
        self._number = number
        self.factors = [1, number]

    def is_factor(self, factor):
        return self._number % factor == 0

    def add_factor(self, factor):
        self.factors.append(factor)

    def get_factors(self):
        # code operates on different levels of abstraction
        factors = []  # can be moved to internal state
        factors.append(1)

        i = 2
        while i < self._number:
            if self.is_factor(i):
                self.add_factor(i)  # this behavior can be tested
            i += 1

        return factors
