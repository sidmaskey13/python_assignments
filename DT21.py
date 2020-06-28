givenString = input('Enter tuple list: ')


def sort_tuple_list_last_element(given_string):
    split_tuples = given_string.strip('[]')
    res = list(eval(split_tuples))
    answer = sorted(res, key=lambda tuples: tuples[-1])
    return str(answer)


print(sort_tuple_list_last_element(givenString))
