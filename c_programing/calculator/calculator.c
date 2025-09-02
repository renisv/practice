#include "main.h"
#include <stdio.h>

void print_hello_world()
{
	printf("Hello world\n");
}

int add(int x, int y)
{
	return x + y;
}

int sub(int x, int y)
{
	return x - y;
}

int mul(int x, int y)
{
	return x * y;
}

int div(int x, int y)
{
	if (y == 0)
	{
		printf("Division by 0 is not allowed.\n");
		return (0);
	}
	
	return x / y;

}