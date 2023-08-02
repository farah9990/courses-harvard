#include <cs50.h>
#include <stdio.h>
void make_blocks(int height);
int main(void)
{
    int height ;
    while (true)
    {

        height = get_int("Height : ");
        if (height > 0 && height <= 8)
        {
            break ;
        }
    }
    make_blocks(height);
}








void make_blocks(int height)
{
    int i, j, r ;
    i = 1 ;
    while (i <= height)
    {
        j = i ;
        r = height - i ;

        while (r > 0)
        {
            printf(" ");
            r-- ;
        }

        while (j > 0)
        {
            printf("#");
            j -- ;
        }

        printf("\n");
        i++ ;
    }

}

