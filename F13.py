givenString = input('Enter string: ')


def reverse_string(given_string):
    split_tuples = given_string.strip('[]')
    into_tuple_list = list(eval(split_tuples))
    sorted_list = sorted(into_tuple_list, key=lambda x: x[-1])

    return sorted_list


print(reverse_string(givenString))