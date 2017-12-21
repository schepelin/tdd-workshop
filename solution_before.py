
def is_perfect(number):
    pass
    # initialize factors
    # check if number a factor <--- simpliest thing to do
    # sum factors


class PerfectNumberClassifier:

    def __init__(self, number):
        self._number = number
        self.factors = {1, number}

    def is_factor(self, factor):
        return self._number % factor == 0

    def add_factor(self, factor):
        self.factors.add(factor)

    def calculate_factors(self):
        for i in range(2, self._number):
            if self.is_factor(i):
                self.add_factor(i)

    def is_perfect(self):
        self.calculate_factors()
        return sum(self.factors) - self._number == self._number
