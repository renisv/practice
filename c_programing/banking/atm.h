#ifndef ATM_H
#define ATM_H

typedef struct
{
    char name[100];
    int accountNumber;
    float balance;
} BankClient;

void viewBalance(BankClient clients[], int size, int accountNumber);
void deposit(BankClient clients[], int size, int accountNumber, float amount);
void withdraw(BankClient clients[], int size, int accountNumber, float amount);


#endif