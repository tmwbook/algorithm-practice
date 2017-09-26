import random

def get_unique_unordered(n):
    """Get n length list"""
    to_return = []
    for _ in range(n):
        x = random.randint(10, 99)
        while x in to_return:
            x = random.randint(0, 100)
        to_return.append(x)
    return to_return