#include <cs50.h>
#include <stdio.h>

void test_credit_number(long credit);

int main(void)
{
    long credit;

    credit = get_long("number : ");
    test_credit_number(credit);


}




void test_credit_number(long credit)
{
    long copy = credit ;
    int fristTwo = 0 ;
    int digit = 0 ;
    int sum1 = 0 ;
    int sum2 = 0 ;
    int i = 0 ;
    while (copy > 0)
    {
        digit = copy % 10 ;
        copy = (copy - digit) / 10 ;
        i++ ;
        if (i % 2 == 0)
        {
            if ((digit * 2) >= 10)
            {
                sum1 += ((digit * 2) % 10) + 1 ;
            }
            else
            {
                sum1 += (digit * 2) ;
            }
        }
        else
        {
            sum2 += digit ;
        }


    }
    int total = sum1 + sum2 ;

    if (total % 10 != 0)
    {
        printf("INVALID\n") ;
    }
    else if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n") ;
    }
    else
    {
        copy = credit ;
        while (copy > 100)
        {
            copy = (copy - (copy % 10)) / 10 ;
            fristTwo = copy ;
        }
        if (fristTwo == 34 || fristTwo == 37)
        {
            printf("AMEX\n") ;
        }
        else if (fristTwo == 51 || fristTwo == 52 || fristTwo == 53  || fristTwo == 54 || fristTwo == 55)
        {
            printf("MASTERCARD\n") ;
        }
        else if (((fristTwo - (fristTwo % 10)) / 10) == 4)
        {
            printf("VISA\n") ;
        }
        else
        {
            printf("INVALID\n") ;
        }
    }
}