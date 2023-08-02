#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text : ");

    // printf("T = %s \n",text) ;

    float  L = 0 ; //average letter per 100 word
    float  S = 0 ; // average sentence per 100 word
    double  X = 0 ;
    int grade = 0 ;

    // printf("l = %i  w = %i s=%i  ",count_letters(text),count_words(text),count_sentences(text)) ;

    L =  count_letters(text) / (float)count_words(text) * 100 ;
    S =  count_sentences(text) / (float)count_words(text) * 100 ;
    X = 0.0588 * L - 0.296 * S - 15.8 ;
    grade = round(X) ;


    if (grade > 16)   // to organize print
    {
        printf("Grade 16+\n") ;
    }
    else if (grade < 1)
    {
        printf(" Before Grade 1\n") ;
    }
    else
    {
        printf("Grade %i\n", grade) ;
    }

}


//mothods


int count_letters(string text) //to count letters in text
{
    int letter = 0 ;
    int k = strlen(text);
    for (int i = 0 ; i <= k ; i++)
    {
        if (isalpha(text[i]))
        {
            letter ++ ;
        }
    }
    return letter ;
}
int count_words(string text)  //to count words in text
{
    int word = 0 ;
    int k = strlen(text);
    for (int i = 0 ; i <= k ; i++)
    {
        if (isspace(text[i]) || text[i] == '\0')
        {
            word ++ ;
        }
    }
    return word ;
}
int count_sentences(string text)      //to count sentence in text
{
    int sentence = 0 ;
    int k = strlen(text);
    for (int i = 0 ; i <= k ; i++)
    {
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            sentence ++ ;
        }
    }
    return sentence ;
}