givenList1 = input('Enter List 1: ')
givenList2 = input('Enter List 2: ')


def intersection_2_list(list1,list2):
    real_list1 = list(eval(list1))
    real_list2 = list(eval(list2))
    answer = list(filter(lambda x: x in real_list1, real_list2))
    return answer


print(intersection_2_list(givenList1, givenList2))