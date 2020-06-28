givenString = input('Enter string: ')


def change_not_poor_to_good(given_string):
    not_postion = 0
    poor_position = 0
    answer = given_string
    answer_string = ""
    split_list = given_string.split()

    for idx, item in enumerate(split_list):
        if item == 'not':
            not_postion = idx
        if idx>not_postion and item == 'poor':
            poor_position = idx
            if poor_position - not_postion == 1 or poor_position - not_postion == 2:
                for i in split_list[:not_postion]:
                    answer_string = answer_string + " " + i
                answer = answer_string + ' good'
    return answer


print(change_not_poor_to_good(givenString))


