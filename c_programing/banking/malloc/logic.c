#include <stdio.h>
#include <stdlib.h>
#include "main.h"

float* create_float_array(int n)
{
    if (n <= 0) 
        return NULL;

    float *arr = (float*)malloc(n * sizeof(float));
    if (arr == NULL) 
        return NULL;

    for (int i = 0; i < n; i++) 
        arr[i] = (float)(i + 1);

    return arr;
}