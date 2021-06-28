class Board:
    def __init__(self):
        self.state = [0,0,0,0,0,0,0,0,0]

    def make_turn(self, pos, player):
        if self.is_valid_turn(pos):
            self.state[pos] = player.symbol
            return True
        return False

    def is_valid_turn(self, pos):
        if self.state[pos] == 0:
            return True
        else:
            return False

    def check_win(self, player):
        s = player.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True
        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True
        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[6] == s and self.state[4] == s and self.state[2] == s:
            return True
        return False

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def print_board(self):
        print(" " + self.convert(self.state[0]) + " | " + self.convert(self.state[1]) + " | " + self.convert(self.state[2]) + " ")
        print(" " + self.convert(self.state[3]) + " | " + self.convert(self.state[4]) + " | " + self.convert(self.state[5]) + " ")
        print(" " + self.convert(self.state[6]) + " | " + self.convert(self.state[7]) + " | " + self.convert(self.state[8]) + " ")

    def convert(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return 'X'
        elif sign == 2:
            return '0'

class Player:

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

if __name__ == '__main__':
    player1 = Player(1, "player1")
    player2 = Player(2, "player2")
    board = Board()
    active_player = player1
    while not board.is_full():
        board.print_board()
        try:
            pos = int(input("Position eingeben [1 - 9]"))
        except ValueError:
            continue
        pos = pos-1
        if pos < 0 and pos > 8:
            print("Bitte Zahl von 0 bis 9 eingeben!")
            continue
        if not board.make_turn(pos, active_player):
            print("ungültiger Zug!")
            continue
        if board.check_win(active_player):
            print(str(active_player.name) + " hat gewonnen!")
            break

        if active_player == player1:
            active_player = player2
        else:
            active_player = player1
    print("Unentschieden!")