givenString = input('Enter list: ')


def check_list_empty(given_string):
    brackets_removed = given_string.strip('[]').strip('()')
    split_list = brackets_removed.split(",")
    # return split_list

    if split_list[0] == "":
        return "list is empty"
    else:
        return "List is not Empty"


print(check_list_empty(givenString))

