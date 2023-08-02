#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0 ; i < height ; i ++) // height for aech pixel
    {
        for (int j = 0 ; j < width ; j ++) // width for aech pixel
        {
            int gray = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0); // to color gray
            image[i][j].rgbtBlue = gray ;
            image[i][j].rgbtGreen = gray ;
            image[i][j].rgbtRed = gray ;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int r, g, b ;
    for (int i = 0 ; i < height ; i ++)
    {
        for (int j = 0 ; j < width ; j ++)
        {
            r = round(image[i][j].rgbtBlue * 0.189 + image[i][j].rgbtGreen * 0.769 + image[i][j].rgbtRed * 0.393);
            g = round(image[i][j].rgbtBlue * 0.168 + image[i][j].rgbtGreen * 0.686 + image[i][j].rgbtRed * 0.349);
            b = round(image[i][j].rgbtBlue * 0.131 + image[i][j].rgbtGreen * 0.534 + image[i][j].rgbtRed * 0.272);
            if (r > 255)
            {
                image[i][j].rgbtRed = 255 ;
            }
            else
            {
                image[i][j].rgbtRed = r ;
            }
            if (g > 255)
            {
                image[i][j].rgbtGreen = 255 ;
            }
            else
            {
                image[i][j].rgbtGreen = g ;
            }
            if (b > 255)
            {
                image[i][j].rgbtBlue = 255 ;
            }
            else
            {
                image[i][j].rgbtBlue = b ;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width] ; //new for get copy
    for (int i = 0 ; i < height ; i ++)
    {
        if (width % 2 == 0)
        {
            for (int j = 0 ; j < width / 2 ; j ++)
            {
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j] ;
            }
        }
        else
        {
            for (int j = 0 ; j < (width - 1) / 2 ; j ++)
            {
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j] ;
            }
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tempImage[height][width];  // new
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tempImage[i][j] = image[i][j];
        }
    }

    for (int i = 0, red, green, blue, counter; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            red = green = blue = counter = 0;
            // + the center pixel
            if (i >= 0 && j >= 0)
            {
                red += tempImage[i][j].rgbtRed;
                green += tempImage[i][j].rgbtGreen;
                blue += tempImage[i][j].rgbtBlue;
                counter++;
            }
            // + below pixel
            if (i >= 0 && j - 1 >= 0)
            {
                red += tempImage[i][j - 1].rgbtRed;
                green += tempImage[i][j - 1].rgbtGreen;
                blue += tempImage[i][j - 1].rgbtBlue;
                counter++;
            }
            // + right pixel
            if ((i >= 0 && j + 1 >= 0) && (i >= 0 && j + 1 < width))
            {
                red += tempImage[i][j + 1].rgbtRed;
                green += tempImage[i][j + 1].rgbtGreen;
                blue += tempImage[i][j + 1].rgbtBlue;
                counter++;
            }
            // + left pixel
            if (i - 1 >= 0 && j >= 0)
            {
                red += tempImage[i - 1][j].rgbtRed;
                green += tempImage[i - 1][j].rgbtGreen;
                blue += tempImage[i - 1][j].rgbtBlue;
                counter++;
            }
            // + left below pixel
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                red += tempImage[i - 1][j - 1].rgbtRed;
                green += tempImage[i - 1][j - 1].rgbtGreen;
                blue += tempImage[i - 1][j - 1].rgbtBlue;
                counter++;
            }
            // + left upper pixel
            if ((i - 1 >= 0 && j + 1 >= 0) && (i - 1 >= 0 && j + 1 < width))
            {
                red += tempImage[i - 1][j + 1].rgbtRed;
                green += tempImage[i - 1][j + 1].rgbtGreen;
                blue += tempImage[i - 1][j + 1].rgbtBlue;
                counter++;
            }
            // + upper pixel
            if ((i + 1 >= 0 && j >= 0) && (i + 1 < height && j >= 0))
            {
                red += tempImage[i + 1][j].rgbtRed;
                green += tempImage[i + 1][j].rgbtGreen;
                blue += tempImage[i + 1][j].rgbtBlue;
                counter++;
            }
            // + below right pixel
            if ((i + 1 >= 0 && j - 1 >= 0) && (i + 1 < height && j - 1 >= 0))
            {
                red += tempImage[i + 1][j - 1].rgbtRed;
                green += tempImage[i + 1][j - 1].rgbtGreen;
                blue += tempImage[i + 1][j - 1].rgbtBlue;
                counter++;
            }
            // + upper right pixel
            if ((i + 1 >= 0 && j + 1 >= 0) && (i + 1 < height && j + 1 < width))
            {
                red += tempImage[i + 1][j + 1].rgbtRed;
                green += tempImage[i + 1][j + 1].rgbtGreen;
                blue += tempImage[i + 1][j + 1].rgbtBlue;
                counter++;
            }

            image[i][j].rgbtRed = round(red / (counter * 1.0));
            image[i][j].rgbtGreen = round(green / (counter * 1.0));
            image[i][j].rgbtBlue = round(blue / (counter * 1.0));
        }
    }


    return;
}

