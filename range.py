class OutOfRangeError(Exception):
    pass

try:
    num = int(input("Enter number"))
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    else:
        raise OutOfRangeError

except OutOfRangeError:
    print("Thats not one of the allowed values!")
    