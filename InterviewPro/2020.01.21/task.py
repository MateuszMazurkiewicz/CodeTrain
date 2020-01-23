'''
Design a Tic-Tac-Toe game played between two players on an n x n grid. A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid. A player who succeeds in placing n of their marks in a horizontal, diagonal, or vertical row wins the game. Once a winning condition is reached, the game ends and no more moves are allowed. Below is an example game which ends in a winning condition:

Given n = 3, assume that player 1 is "X" and player 2 is "O" 
board = TicTacToe(3);

board.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

board.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

board.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

board.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

board.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

board.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

board.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|


Here's a starting point:
'''

class TicTacToe(object):
    def __init__(self, n):
        self.board = []
        self.n = n
        for _ in range(n):
            self.board.append([0] * n)

    def move(self, row, col, player):
        self.board[row][col] = -1 + 2 * (player - 1)
        result = self.check()
        if result:
            return player

    def check(self):
        return self.check_diagonal or self.check_horizontal or self.check_vertical
    # Fill this in.

    def check_horizontal(self):
        for i in range(self.n):
            if abs(sum(self.board[i])) == self.n:
                return True
        return False

    def check_vertical(self):
        for i in range(self.n):
            tmp = 0
            for j in range(self.n):
                tmp += self.board[j][i]
            if abs(tmp) == self.n:
                return True

        return False

    def check_diagonal(self):
        tmp_1 = 0
        tmp_2 = 0
        for i in range(self.n): 
            tmp_1 += self.board[i][i]
            tmp_2 += self.board[self.n - i - 1][self.n - i - 1]
        if abs(tmp_1) == self.n or abs(tmp_2) == self.n:
            return True

        return False

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))