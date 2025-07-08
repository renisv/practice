void initializeBoard(char board[3][3]);
void displayBoard(char board[3][3]);
int isValidMove(char board[3][3], int row, int col);
int checkWin(char board[3][3], char player);
int isBoardFull(char board[3][3]);
void playTurn(char board[3][3], char player);