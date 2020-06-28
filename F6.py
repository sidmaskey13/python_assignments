givenNumber = int(input('Enter a number: '))
upperRange = int(input('Enter upper range: '))
lowerRange = int(input('Enter lower range: '))


def number_in_range(given_number, upper_range, lower_range):
    range_list = [i for i in range(lower_range, upper_range+1)]
    if given_number in range_list:
        return f"{given_number} is in the range"
    else:
        return f"{given_number} is not in the range"


print(number_in_range(givenNumber, upperRange, lowerRange))

