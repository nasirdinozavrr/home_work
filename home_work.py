class Algorithm:
    def __init__(self, numbers, desired_sum):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def print_algorithm(self):
        for n in self.numbers:
            for d in self.numbers[self.numbers.index(n) + 1:]:
                if n + d == self.desired_sum:
                    return (self.numbers.index(n),self.numbers.index(d))


algorithm = Algorithm(numbers=[2, 7, 11, 15], desired_sum=9)




print(algorithm.print_algorithm())
