from functools import reduce

givenNumber = int(input('Enter number: '))


def fibonacci_series(given_number):
    return reduce(lambda x, _: x + [x[-1] + x[-2]], range(given_number - 2), [0, 1])


print(fibonacci_series(givenNumber))