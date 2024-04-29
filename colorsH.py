import random


color = random.randrange(0, 2**24)


hex_color = hex(color)

print(hex_color)


import random

color = random.randrange(0, 2**24)


hex_color = hex(color)

std_color = "#" + hex_color[2:]

print(std_color)
import secrets


s = ""


x = 0


while x < 6:

    s += secrets.choice("0123456789ABCDEF")
    x += 1


print(s)
import secrets


s = secrets.token_hex(3)

print(s)
import randomcolor


color = randomcolor.RandomColor().generate()
print(color)

from webcolors import name_to_hex


def color_name_to_code(color_name):

    try:

        color_code = name_to_hex(color_name)

        return color_code

    except ValueError:

        return None


colorname = input("Enter color name : ")


result_code = color_name_to_code(colorname)


print(result_code)
