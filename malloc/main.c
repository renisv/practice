#include <stdio.h>
#include <stdlib.h>
#include "main.h"

int main() 
{
    const int size = 4;
    float *numbers = create_float_array(size);
    
    if (numbers == NULL) 
    {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Allocated array: ");
    for (int i = 0; i < size; i++) 
    {
        printf("%.1f ", numbers[i]);
    }
    printf("\n");

    free(numbers);
    numbers = NULL;
    
    return 0;
}