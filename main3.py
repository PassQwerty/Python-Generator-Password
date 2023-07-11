import random


def GetPassword(Length):
    password = ""
    for _ in range(Length):
        letter = chr(random.randrange(33, 127))
        password += letter

    return password


print(GetPassword(7))
