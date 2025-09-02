#include <stdio.h>
#include "atm.h"
#include <string.h>

void viewBalance(BankClient clients[], int size, int accountNumber)
{
    int i; 
    for (i=0; i < size; i++)
    {
        if (clients[i].accountNumber == accountNumber)
        {
            printf("Account balance for %s: %.2f.\n", clients[i].name, clients[i].balance);
            return;
        }
    }
    printf("Please enter correct account number.\n");
}


void deposit(BankClient clients[], int size, int accountNumber, float amount)
{
    int i;
    for (i=0; i < size; i++)
    {
        if (clients[i].accountNumber == accountNumber)
        {
            clients[i].balance += amount;
            printf("Deposited %.2f. New balance: %.2f\n", amount, clients[i].balance);
            return;
        }
    }
    printf("Please enter correct account number.\n");
}

void withdraw(BankClient clients[], int size, int accountNumber, float amount)
{
    int i;
    for (i=0; i < size; i++)
    {
        if (clients[i].accountNumber == accountNumber)
        {
            if (clients[i].balance >= amount)
            {
               clients[i].balance -= amount;
               printf("Withdrawn %.2f. New balance: %.2f\n", amount, clients[i].balance);
               return; 
            }
            else
            {
                printf("Insuffiecient funds.\n");
                return;
            }
        }
    }
    printf("Please enter correct account number.\n");
}