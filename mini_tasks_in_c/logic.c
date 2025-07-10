#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "main.h"

char *password_generator(int length)
{
    const char charset[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char *password = malloc(sizeof(char) * length + 1);
    const int charsetSize = sizeof(charset) - 1;
    
    for (int i = 0; i < length; i++) {
        int index = rand() % charsetSize;
        password[i] = charset[index];
    }
    password[length] = '\0'; 

    return (password);

}

int validate_username(char *username)
{
    int i;

    if (strlen(username) < 5) 
        return (0);
    
    for (i = 0; i < strlen(username); i++)
    {
        if ((username[i] >= '0' && username[i] <= '9') && (username[i] >= 'a' && username[i] <= 'z') && (username[i] >= 'A' && username[i] <= 'Z'))
            return (1);
    }

    return (0);

}
