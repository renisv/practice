#include "main.h"
#include <stdio.h>
#include <string.h>

int main(void)
{
    MenuItem menu[10];
    int size = 0;
    addMenuItem(menu, &size, "Berxolle", 8.5 , 0);
    addMenuItem(menu, &size, "Biftek", 10.5 , 0);
    addMenuItem(menu, &size, "Tomahok", 29.9 , 0);
    addMenuItem(menu, &size, "Paidhaqe", 19.9 , 0);
    
    displayMenu(menu, size);

    searchMenuItem(menu, size, "Tomahok");

    updateMenuItemPrice(menu, size, "Paidhaqe", 12);
    
    displayMenu(menu, size);

    setItemAvailability(menu, size, "Paidhaqe", 1);

    displayMenu(menu, size);

    return (0);
}