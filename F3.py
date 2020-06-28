from functools import reduce
givenString = input('Enter list: ')


def mutliply_list(given_string):
    brackets_removed = list(eval(given_string))
    int_list = [int(i) for i in brackets_removed]
    answer = reduce(lambda x, y: x * y, int_list)
    return answer


print(mutliply_list(givenString))