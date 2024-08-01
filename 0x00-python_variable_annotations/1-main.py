#!/usr/bin/env python3

concat = __import__('1-concat').concat
print(concat("hello", " Zaid"))
print(concat.__annotations__)
