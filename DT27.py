givenList1 = input('Enter List 1: ')
givenList2 = input('Enter List 2: ')


def add_string_list(given_list1, given_list2):
    real_given_list_1 = list(eval(given_list1))
    real_given_list_2 = list(eval(given_list2))
    new_list = real_given_list_1[:-1]
    for i in real_given_list_2:
        new_list.append(i)
    return new_list


print(add_string_list(givenList1, givenList2))