import random
import string


def GetPassword(Length):
    # Генератор на спецсимволах ( !@#$%^& ) + ascii_lowercase
    words = ["!", "@", "#", "$", "%", "^", "&"]
    letters = string.ascii_lowercase
    rand_string = ''.join(
        random.choice(
            [random.choice(letters), random.choice(words)]
        )
        for i in range(Length))
    return f"Random string of length {Length} is {rand_string}"


print(GetPassword(7))
