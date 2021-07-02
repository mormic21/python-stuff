from functools import partial

def mal(x, y):
    return x*y

mal2 = partial(mal, 2)
print(mal2(5))
