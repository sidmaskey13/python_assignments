givenString = input('Enter String: ')
dictionary = dict()


def count_words(given_string):
    split_words = given_string.split()
    for each_word in split_words:
        each_count = split_words.count(each_word)
        dictionary.update({each_word: each_count})
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    answer = dict(sorted_list)
    return answer


print(count_words(givenString))