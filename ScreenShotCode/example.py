import math

def addIf(a, b, adding):
    return a + b if adding else 0


if __name__ == "__main__":
    # This is a signal line comment
    """This is a
    multi line comment
    """

    x = int(input("Insert x value: "))
    y = int(input("Insert x value: "))
    adding = True

    print(addIf(x, y, adding))
