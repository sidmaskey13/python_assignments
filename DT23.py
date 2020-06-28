givenString = input('Enter list: ')


def check_list_empty(given_string):
    given_list = list(eval(given_string))

    if not given_list:
        return "list is empty"
    else:
        return "List is not Empty"


print(check_list_empty(givenString))

