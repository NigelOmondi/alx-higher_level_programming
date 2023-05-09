#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':  # check if c is lowercase
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)  # add a newline after the last character
