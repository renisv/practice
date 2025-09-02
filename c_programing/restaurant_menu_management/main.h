#ifndef MAIN_H
#define MAIN_H

typedef struct {
    char name[50];
    float price;
    int available;
} MenuItem;

void addMenuItem(MenuItem menu[], int *size, char name[], float price, int available);
void displayMenu(MenuItem menu[], int size);
int searchMenuItem(MenuItem menu[], int size, char name[]);
void updateMenuItemPrice(MenuItem menu[], int size, char name[], float newPrice);
void setItemAvailability(MenuItem menu[], int size, char name[], int available);

#endif

