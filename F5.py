from functools import reduce

givenNumber = int(input('Enter number: '))


def factorial_number(given_number):
    answer = reduce(lambda x, y: x*y, [i for i in range(1, given_number+1)])
    return answer


print(factorial_number(givenNumber))