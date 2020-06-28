givenString = input('Enter string: ')


def reverse_string(given_string):
    answer = ""
    for i in reversed(given_string):
        answer += i
    return answer


print(reverse_string(givenString))