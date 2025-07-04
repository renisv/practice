#include "atm.h"
#include <stdio.h>

int main(void)
{
    BankClient clients[] = 
    {
        {"Alba", 1, 2000.5}, 
        {"Sokol", 2, 1800},
        {"Renis", 3, 700},
        {"Enea", 4, 500}
    };

    int size = sizeof(clients) / sizeof(BankClient);

    viewBalance(clients, size, 1);
    deposit(clients, size, 1, 200);
    withdraw(clients, size, 1, 700);

    return 0;
}