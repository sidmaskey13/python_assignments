givenList = input('Enter List: ')
givenString = input('Enter string: ')


def add_string_list(given_list, given_string):
    new_list = []
    given_list_to_add_string = given_list.replace(" ","").strip("()").strip("[]")
    split_list = given_list_to_add_string.split(",")
    new_list = [given_string+i for i in split_list]
    return new_list


print(add_string_list(givenList, givenString))