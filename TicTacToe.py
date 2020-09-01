
# Author: Jun Kim
# Date:03/02/2020
# Description: Program for a TicTacToe Game.


# define class TicTacToe
class TicTacToe:
    """Represents two private data members: the board and the current state."""
    def __init__(self):
        """initializes the board"""
        self._board = [["_","_","_"],["_","_","_"],["_","_","_"]]
        self._current_state = "UNFINISHED"
        self._counter = 0

    def get_current_state(self):
        """Returns current state"""
        return self._current_state

    def display_board(self):
        print(self._board[0][0] + "|" + self._board[0][1] + "|" + self._board[0][2])
        print(self._board[1][0] + "|" + self._board[1][1] + "|" + self._board[1][2])
        print(self._board[2][0] + "|" + self._board[2][1] + "|" + self._board[2][2])

    def make_move (self,row,column,symbol):
        """player x or o makes move and mutates the board, until a win or a draw is made"""

        if row >=0 and row <=2 and column >=0 and column <=2:

            # while loop until someone wins, or it draws
            while self._current_state == "UNFINISHED":

                #if the space is already occupied, return false
                if self._board[row][column] == "o":
                    return False
                if self._board[row][column] == "x":
                    return False

                self._board[row][column] = symbol
                self._counter += 1 #adds count to number of moves
                self.display_board()
                print("")

                if self._board[row][0] == symbol and self._board[row][1] == symbol and self._board[row][2] == symbol:
                    self._current_state = str.upper(symbol) + "_WON" # winning by a horizontal line

                elif self._board[0][column] == symbol and self._board[1][column] == symbol and self._board[2][column] == symbol:
                    self._current_state = str.upper(symbol) + "_WON" # winning by a vertical line
                elif self._board[0][0] == symbol and self._board[1][1] == symbol and self._board[2][2] == symbol:
                    self._current_state = str.upper(symbol) + "_WON" # winning by a diagonal line top left to bottom right
                elif self._board[0][2] == symbol and self._board[1][1] == symbol and self._board[2][0] == symbol:
                    self._current_state = str.upper(symbol) + "_WON"  # winning by a diagonal line top right to bottom left
                else:
                    if self._counter >= 9 and self._current_state == "UNFINISHED": # 9 moves means all the spaces are filled, if game is still unfinished, it's a draw
                        self._current_state = "DRAW"
                return True
            else:
                return False
        else:
            return False

