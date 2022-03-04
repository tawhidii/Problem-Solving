# def skip_elements(elements):
#     # code goes here
#     result = []
#     for idx, element in enumerate(elements):
#         if idx % 2 == 0:
#             result.append(element)

#     return result


# # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


# def show_email(peoples):
#     result = []
#     for people in peoples:
#         email, name = people
#         result.append('{}<{}>'.format(name, email))
#     return result


# print(show_email([('bari@gmail.com', 'bari'), ('tawhidi@gmail.com',
#                                                'tawhidi'), ('khademul@mail.com', 'khademul')]))
# def guest_list(guests):
#     for g in guests:
#         name, age, occu = g
#         print("{} is {} years old and works as {}".format(name, age, occu))


# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
#            ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    print(result)


count_letters('hello')
