from pygame.locals import *
import pygame
import time


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
        # draw an x or o
        self.board[row][col] = player.char
        return (row, col)

    def board_pos(self, mouse_x, mouse_y, player):
        # determine the row the user clicked
        if (mouse_y < 100):
            row = 0
        elif (mouse_y < 200):
            row = 1
        else:
            row = 2

        # determine the column the user clicked
        if (mouse_x < 100):
            col = 0
        elif (mouse_x < 200):
            col = 1
        else:
            col = 2

        # return the tuple containg the row & column
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
        return False

    def check_tie(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.board[i][j] is None):
                    return False
        return True


class Player:
    def __init__(self, num, char):
        self.num = num
        self.char = char


class App:
    def __init__(self):
        self.window_width = 300
        self.window_height = 325
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player1 = Player(1, 'x')
        self.player2 = Player(2, 'o')
        self.board = Board()

    def on_init(self):
        pygame.init()
        self._running = True
        self._display_surf = pygame.display.set_mode((self.window_width,
                                                      self.window_height))
        pygame.display.set_caption('Tic Tac Toe')

        # set up the background surface
        self._image_surf = pygame.Surface(self._display_surf.get_size())
        self._image_surf = self._image_surf.convert()
        self._image_surf.fill((0, 0, 0))

        # draw the grid lines
        # vertical lines
        pygame.draw.line(self._image_surf,
                         (255, 255, 255), (100, 0), (100, 300), 1)
        pygame.draw.line(self._image_surf,
                         (255, 255, 255), (200, 0), (200, 300), 1)

        # horizontal lines
        pygame.draw.line(self._image_surf,
                         (255, 255, 255), (0, 100), (300, 100), 1)
        pygame.draw.line(self._image_surf,
                         (255, 255, 255), (0, 200), (300, 200), 1)

    def on_quit(self):
        self._running = False

    def on_render(self, message):
        font = pygame.font.Font(None, 25)
        text = font.render(message, 1, (255, 255, 255))
        self._image_surf.fill((0, 0, 0), (0, 300, 300, 25))
        self._image_surf.blit(text, (80, 305))
        self._display_surf.blit(self._image_surf, (0, 0))
        pygame.display.flip()

    def is_winner(self):
        return self.board.check_win()

    def is_tie(self):
        return self.board.check_tie()

    def on_cleanup(self):
        pygame.quit()

    def draw_move(self, row, col, player):
        # determine the center of the square
        center_x = ((col) * 100) + 50
        center_y = ((row) * 100) + 50

        # draw the appropriate piece
        if (player.char == 'o'):
            pygame.draw.circle(self._image_surf,
                               (0, 0, 255), (center_x, center_y), 45, 2)
        else:
            pygame.draw.line(self._image_surf, (255, 0, 0),
                             (center_x - 45, center_y - 45),
                             (center_x + 45, center_y + 45), 2)
            pygame.draw.line(self._image_surf, (255, 0, 0),
                             (center_x + 45, center_y - 45),
                             (center_x - 45, center_y + 45), 2)

    def on_execute(self):
        if (self.on_init() is False):
            self._running = False
        turn = self.player1
        message = "It's player " + str(turn.num) + "'s turn"
        self.on_render(message)
        while (self._running):
            for event in pygame.event.get():
                if (event.type is QUIT):
                    self.on_quit()
                elif (event.type is MOUSEBUTTONDOWN):
                    (row, col) = self.board.click_board(turn)
                    if (row is not None and col is not None):
                        self.draw_move(row, col, turn)
                    if (self.is_winner()):
                        message = "Player " + str(turn.num) + " wins the game!"
                        self.on_render(message)
                        self.on_quit()
                    elif(self.is_tie()):
                        message = "It's a tie!"
                        self.on_render(message)
                        self.on_quit()
                    else:
                        if (turn is self.player1):
                            turn = self.player2
                        else:
                            turn = self.player1
                        message = "It's player " + str(turn.num) + "'s turn"
                        self.on_render(message)
        time.sleep(3)
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
