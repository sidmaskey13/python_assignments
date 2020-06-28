givenString = input('Enter string: ')


def longest_word(given_string):
    split_words = given_string.split()
    longest_length = 0

    for word in split_words:
        length = len(word)
        if longest_length <= length:
            longest_length = length
    return f"""Longest word's length is {longest_length}"""


print(longest_word(givenString))


