from pygame.locals import *
import pygame

class Board:
    def __init__(self):
        self.board = [[None, None, None],
                [None, None, None],
                [None, None, None]]

    def click_board(self, player):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        (row, col) = self.board_pos(mouse_x, mouse_y, player)

        # make sure no one's used this space
        if ((self.board[row][col] == "x") or (self.board[row][col] == "o")):
            # this space is in use
            return (None, None)

        # draw an x or an o
        self.board[row][col] = player.char
        return (row, col)

    def board_pos(self, mouse_x, mouse_y, player):
        # determine the row the user clicked
        if mouse_y < 100:
            row = 0
        elif mouse_y < 200:
            row = 1
        else:
            row = 2

        # determine the column the user clicked
        if mouse_x < 100:
            col = 0
        elif mouse_x < 200:
            col = 1
        else:
            col = 2

        # return the tuple containing the row and the column
        return (row, col)

    def check_win(self):
        for row in range(0, 3):
            if ((self.board[row][0] == self.board[row][1] ==
                 self.board[row][2]) and (self.board[row][0] is not None)):
                # this row won
                return True

        # check for winning columns
        for col in range(0, 3):
            if (self.board[0][col] == self.board[1][col] ==
                    self.board[2][col]) and (self.board[0][col] is not None):
                # this column won
                return True

        # check for diagonal winners
        if (self.board[0][0] == self.board[1][1] ==
                self.board[2][2]) and (self.board[0][0] is not None):
            # game won diagonally left to right
            return True

        if (self.board[0][2] == self.board[1][1] ==
                self.board[2][0]) and (self.board[0][2] is not None):
            # game won diagonally right to left
            return True

        # player did not win
        return False

    def check_tie(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.board[i][j] is None):
                    # it is not a tie
                    return False

        # it is a tie
        return True


