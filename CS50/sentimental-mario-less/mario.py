# TODO
from cs50 import get_int


# to show program in up

def main():
    while True:
        height = get_int("Height : ")
        if height > 0 and height <= 8:
            break
    make_blocks(height)


# method to more orgnaize

def make_blocks(height):
    i = 1
    while i <= height:
        j = i
        r = height - i
        while r > 0:
            print(" ", end="")
            r -= 1
        while j > 0:
            print("#", end="")
            j -= 1
        print()
        i += 1


# in real begin here
main()
