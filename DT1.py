givenString = input('Enter String: ')
dictionary = dict()


def count_characters(given_string):
    for each_letter in given_string:
        each_count = given_string.count(each_letter)
        dictionary.update({each_letter: each_count})
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    answer = dict(sorted_list)
    return answer


print(count_characters(givenString))