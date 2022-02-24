import re
from turtle import clear


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


ans = monkey_trouble(True, False)
print(ans)
