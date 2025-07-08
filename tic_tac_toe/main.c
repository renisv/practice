#include <stdio.h>
#include "tic_tac_toe.h"

int main() {
    char board[3][3];
    char currentPlayer = 'X';  // Start with player X

    initializeBoard(board);  // Initialize the game board

    while (1) {
        displayBoard(board);  // Show the current board
        playTurn(board, currentPlayer);  // Get the current player's move

        if (checkWin(board, currentPlayer)) {
            displayBoard(board);  // Show the final board
            printf("Player %c wins!\n", currentPlayer);
            break;
        }

        if (isBoardFull(board)) {
            displayBoard(board);  // Show the final board
            printf("It's a draw!\n");
            break;
        }

        // Switch to the next player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}