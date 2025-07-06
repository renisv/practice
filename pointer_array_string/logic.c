#include <stdio.h>
#include "main.h"

int count_vowel(char *str)
{
    int i,j;
    int count = 0;
    char vowel[] = "aeiouyAEIOUY";
    for (i = 0; str[i] != '\0'; i++)
    {
        for (j = 0; vowel[j] != '\0'; j++)
        {
            if (str[i] == vowel[j])
            {
                count++;
                break;
            }
        }
    }
    return count;
}

void swap_int(int *num1, int *num2)
{
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}

int find_min(int arr[], int size)
{
    if (size <= 0) {
        return 0; 
    }

    int min = arr[0]; 
    
    for (int i = 1; i < size; i++) {
        if (arr[i] < min) {
            min = arr[i]; 
        }
    }
    
    return min;
}

void reverse_string(char *str) 
{
    if (str == NULL || *str == '\0') return;
    
    char *end = str;
    for (; *end != '\0'; end++) {}
    end--;
    
    for (char *start = str; start < end; start++, end--) 
    {
        char temp = *start;
        *start = *end;
        *end = temp;
    }
    printf("%s\n", str);
}

int *find_value(int *arr, int size, int target)
{
    int i;
    int *ptr;
    for (i = 0; i < size; i++)
    if (arr[i] == target)
        return &arr[i];
    printf("%p\n", ptr);
    return (NULL);
}