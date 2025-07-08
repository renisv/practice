#include <stdio.h>
#include "tic_tac_toe.h"

void initializeBoard(char board[3][3])
{
    int i, j;
    
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            board[i][j] = ' ';
        }
    }
}

void displayBoard(char board[3][3])
{
    int i, j;
    
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%c ", board[i][j]);
        }   
        printf("\n");
    }
}

int isValidMove(char board[3][3], int row, int col)
{
    if ((row >= 0 && row < 3) && (col >= 0 && col < 3) && board[row][col] == ' ')
        return (1);
    return (0);
}

int checkWin(char board[3][3], char player)
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
            return (1);
    }

    for (j = 0; j < 3; j++)
    {
        if (board[0][j] == player && board[1][j] == player && board[2][j] == player)
            return (1);
    }

    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
        return (1);

    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
        return (1);

    return(0);
}

int isBoardFull(char board[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (board[i][j] == ' ')
                return (0);
        }
    }
    return (1);
}

void playTurn(char board[3][3], char player)
{
    int row, col;

    printf("Enter row and column (values between 0 and 2)\n");
    scanf("%d %d", &row, &col);

    if (isValidMove(board, row, col))
        board[row][col] = player;
    else 
        printf("Invalid move\n");
}