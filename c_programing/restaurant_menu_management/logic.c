#include "main.h"
#include <stdio.h>
#include <string.h>

void addMenuItem(MenuItem menu[], int *size, char name[], float price, int available)
{
    strcpy(menu[*size].name, name);
    menu[*size].price = price;
    menu[*size].available = available;
    (*size)++;
}

void displayMenu(MenuItem menu[], int size)
{
    int i = 0;
    for (i=0; i < size; i++)
    {
        printf("*-%s,  %.2f$, %d\n", menu[i].name, menu[i].price, menu[i].available);
    }
}

int searchMenuItem(MenuItem menu[], int size, char name[])
{
    int i = 0;
    for (i=0; i < size; i++)
    {
        if (strcmp(menu[i].name,name) == 0)
        {
            printf("This product is on the menu.\n");
            return (i);
        }
    }
    printf("This product is not on the menu.\n");
    return (-1);
}


void updateMenuItemPrice(MenuItem menu[], int size, char name[], float newPrice)
{
    int i = 0;
    for (i=0; i < size; i++)
    {
        if (strcmp(menu[i].name,name) == 0)
        {
            menu[i].price = newPrice;
        }
    }
}

void setItemAvailability(MenuItem menu[], int size, char name[], int available)
{
    int i = 0;
    for (i=0; i < size; i++)
    {
        if (strcmp(menu[i].name,name) == 0)
        {
            menu[i].available = available;
        }
    }
}