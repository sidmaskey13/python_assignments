givenNumber = int(input('Enter number: '))


def reverse_string(given_number):
    prime = 0
    for i in range(1,given_number):
        if given_number % i == 0:
            prime +=1

    if prime < 2:
        return f"{given_number} is Prime Number"
    else:
        return f"{given_number} is not Prime Number"


print(reverse_string(givenNumber))