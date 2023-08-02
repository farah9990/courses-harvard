#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

bool only_digits(string); //prototype
int rotate(char, int);
int main(int argc, string argv[])
{

    if (argc == 2) // check if one command line
    {
        if (only_digits(argv[1])) // check if numaric
        {
            int length = strlen(argv[1]);
            int k = atoi(argv[1]) ;
            string text = get_string("plaintext: ");
            int l = strlen(text);
            printf("ciphertext: ");
            int c ;
            for (int i = 0 ; i < l ; i++) // to print caesar
            {
                if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
                {
                    c = rotate(text[i], k);
                    printf("%c", c);
                }
                else
                {
                    c = text[i];
                    printf("%c", c);
                }

            }
            printf("\n");
            return 0 ;
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1 ;
        }


    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1 ;
    }

}


bool only_digits(string t) //method to check if digit
{
    int length = strlen(t);
    for (int i = 0 ; i < length ; i++) //check all
    {
        if (isdigit(t[i]))
        {
            if (i + 1 == length) // for just return if all is numaric
            {
                return true ;
            }
        }
    }
    return false ;
}

int rotate(char c, int k) // check if char upper or lower and retern caesar
{
    int caesar ;
    if (isupper(c))
    {
        caesar = ((((int)c + k) - 65) % 26) + 65;
    }
    else
    {
        caesar = ((((int)c + k) - 97) % 26) + 97;
    }
    return caesar ;
}