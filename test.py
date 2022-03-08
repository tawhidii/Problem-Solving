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


# def count_letters(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     print(result)


# count_letters('hello')

# wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
# for key, value in wardrobe.items():
#     for color in value:
#         print('{} {}'.format(color, key))


# def email_list(domains):
#     emails = []
#     for domain, users in domains.items():
#         for user in users:
#             emails.append('{}@{}'.format(user, domain))
#     return(emails)


# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
#       "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# def add_prices(basket):
#     # Initialize the variable that will be used for the calculation
#     total = 0
#     # Iterate through the dictionary items
#     for _, value in basket.items():
#         # Add each price to the total calculation
#         # Hint: how do you access the values of
#         # dictionary items?
#         total += value
#     # Limit the return value to 2 decimal places
#     return round(total, 2)


# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
#              "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries))  # Should print 28.44
