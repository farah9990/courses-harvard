#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        FILE *file = fopen(argv[1], "r");
        // if one command-line argument
        if (!argv[1])
        {
            printf("file does not exists\n");
            return 1;
        }
        BYTE buffer[512];
        int count = 0 ;
        char filename[8] = {0};
        FILE *output = NULL;
        while (fread(buffer, 1, sizeof(buffer), file) != 0)
        {

            // check if beginning of jpeg file
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                // if already found a jpeg, close the file
                if (count > 0)
                {
                    fclose(output);
                }
                // name file
                sprintf(filename, "%03i.jpg", count);
                // open file
                output = fopen(filename, "w");
                count++;
            }
            if (output != NULL)
            {
                // writing
                fwrite(buffer, 1, sizeof(buffer), output);
            }
        }
        fclose(output);
        fclose(file);
    }
    else
    {
        printf("Usage: ./recover IMAGE\n");
        return 1 ;
    }
}
