givenString = input('Enter list: ')


def sum_list(given_string):
    brackets_removed = given_string.strip('[]').strip("()").split(",")
    int_list = [int(i) for i in brackets_removed]
    answer = sum(int_list)
    return answer


print(sum_list(givenString))
