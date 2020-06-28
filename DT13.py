givenString = input('Enter string: ')


def sort_comma_words(given_string):
    new_list= []
    split_words = given_string.split(', ')
    for word in reversed(split_words):
        new_list.append(word)
    return new_list


print(sort_comma_words(givenString))