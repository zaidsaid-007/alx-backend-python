#!usr/bin/env python3

to_str = __import__('3-to_str').to_str
pi_str = to_str(7.56749)
print(to_str(7.56749))
print(to_str.__annotations__)
print("to_str(7.56749) returns {} which is a {}".format(pi_str, type(pi_str)))