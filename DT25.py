givenString = input('Enter string: ')


def dictionary_empty(given_string):
    real_dictionary = eval(given_string)
    if not bool(real_dictionary):
        return "Empty Dictionary"
    else:
        return "Not Empty Dictionary"


print(dictionary_empty(givenString))