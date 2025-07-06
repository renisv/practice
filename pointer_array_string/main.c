#include <stdio.h>
#include "main.h"

int main(void)
{
    char str[] = {"String Test"};
    int result = count_vowel(str);
    printf("The number of vowels in the string %s is %d.\n", str, result);

    int a = 5, b = 10;
    printf("Before: a = %d, b = %d\n", a, b);
    swap_int(&a, &b);
    printf("After: a = %d, b = %d\n", a, b);

    int numbers[] = {34, 12, 56, 2, 89};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    int minimum = find_min(numbers, size);
    printf("The smallest number is: %d\n", minimum);

    reverse_string(str);

    find_value(numbers,size,34);
    
}
