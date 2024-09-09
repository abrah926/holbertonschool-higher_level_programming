#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

    print("{c} is {case}".format(c=c, case="lower" if islower(c) else "upper"))
