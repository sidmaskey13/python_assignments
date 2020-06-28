givenNumber = int(input('Enter number: '))


def filter_lambda(given_number):
    mul_list = [i for i in range(1,100)]
    sorted_list = list(filter(lambda x: x % given_number == 0, mul_list))
    return sorted_list


print(filter_lambda(givenNumber))