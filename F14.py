givenDictionary =[
    {"name": "Sid", "age": 20},
    {"name": "Sid", "age": 5},
    {"name": "Ajay", "age": 20},
    {"name": "Sam", "age": 20},
    {"name": "Ram", "age": 22},
    {"name": "Shyam", "age": 11}
    ]


def sort_dictionary(given_string):
    sorted_list = sorted(given_string, key=lambda i: (i['name'], i['age']))
    return sorted_list


print(sort_dictionary(givenDictionary))