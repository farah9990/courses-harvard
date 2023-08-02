# TODO
from cs50 import get_int


# method to show program to up
def main():
    credit = get_int("number : ")
    test_credit_number(credit)


# method to test credit
def test_credit_number(credit):
    copy = credit
    digit = 0
    sum1 = 0
    sum2 = 0
    i = 0
    while copy > 0:
        digit = copy % 10
        copy = (copy - digit) / 10
        i += 1
        if i % 2 == 0:
            if digit * 2 >= 10:
                sum1 += ((digit * 2) % 10) + 1
            else:
                sum1 += (digit * 2)
        else:
            sum2 += digit

    total = sum1 + sum2

    # test if valid
    if total % 10 != 0:
        print("INVALID")
    elif i != 13 and i != 15 and i != 16:
        print("INVALID")
    else:

        # it is valid and we get frist two number
        copy = credit
        while copy > 100:
            copy = (copy - (copy % 10)) / 10
            fristTwo = copy

        # show type of credit
        if fristTwo == 34 or fristTwo == 37:
            print("AMEX")
        elif fristTwo == 51 or fristTwo == 52 or fristTwo == 53 or fristTwo == 54 or fristTwo == 55:
            print("MASTERCARD")
        elif ((fristTwo - (fristTwo % 10)) / 10) == 4:
            print("VISA")
        else:
            print("INVALID")


main()