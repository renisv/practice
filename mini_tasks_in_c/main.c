#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "main.h"

int main(void)
{
    // int length;
    // printf("How long would you like the password to be?\n");
    // scanf("%d", &length);
    // printf("YOur password is %s\n", password_generator(length));

    char *username = "renis***";
    int result = validate_username(username);

    if (result == 0)
        printf("Username must be longer than 5 characters and must not contain symbols, only numbers and letters\n");
    else
        printf("The username %s is valid.\n", username);

}

