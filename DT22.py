givenString = input('Enter list: ')


def remove_duplicates_from_list(given_string):
    brackets_removed = list(eval(given_string))
    answer = []
    [answer.append(x) for x in brackets_removed if x not in answer]
    return answer


print(remove_duplicates_from_list(givenString))


