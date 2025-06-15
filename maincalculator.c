#include <stdio.h>
#include "main.h"

int main(void)
{
	int num1, num2, choice;

	printf("Welcome to my first calculator\n");

	printf("Enter the first number: ");
	scanf("%d", &num1); 
	printf("Enter the second number: ");
	scanf("%d", &num2); 

	do {
		printf("Select mathematical operation\n");
		printf("Press 1 for addition\n");
		printf("Press 2 for substraction\n");
		printf("Press 3 for multiplication\n");
		printf("Press 4 for division\n");
		printf("Press 0 for exit\n");

		scanf("%d", &choice);

		if (choice == 1)
			printf("%d + %d = %d\n", num1, num2, add(num1, num2));
		else if (choice == 2)
			printf("%d - %d = %d\n", num1, num2, sub(num1, num2));
		else if (choice == 3)
			printf("%d * %d = %d\n", num1, num2, mul(num1, num2));
		else if (choice == 4)
			printf("%d / %d = %d\n", num1, num2, div(num1, num2));
		else if (choice == 0)
			printf("Goodbye\n");
		else 
			printf("Invalid choice\n");

		
	} while(choice != 0);

	return (0);

}