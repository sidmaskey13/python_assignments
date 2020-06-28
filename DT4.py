firstString = input('Enter first string: ')
secondString = input('Enter second string: ')


def exchange_combine(first_string, second_string):
    first_string_first_two = first_string[:2]
    second_string_first_two = second_string[:2]
    first_word = first_string_first_two + second_string[2:]
    second_word = second_string_first_two + first_string[2:]
    combined_word = second_word + " " + first_word
    return combined_word


print(exchange_combine(firstString, secondString))