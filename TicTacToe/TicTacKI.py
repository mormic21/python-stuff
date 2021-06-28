import random

class Board:
    def __init__(self):
        self.state = [0,0,0,0,0,0,0,0,0]
        self.rate = [0,0,0,0,0,0,0,0,0]

    def ki_valid_turns(self):
        for i in range(0,8):
            if self.is_valid_turn(i):
                self.rate[i] = 0
            else:
                self.rate[i] = -5

    def ki_all_moves(self):
        if self.is_valid_turn(4):
            self.rate[4] = 19
        #check verteidigung
        s = Player.players[0]
        #reihen
        if self.state[0] == s and self.state[1] == s:
            if self.is_valid_turn(2):
                self.rate[2] == 30
        if self.state[0] == s and self.state[2] == s:
            if self.is_valid_turn(1):
                self.rate[1] == 30
        if self.state[1] == s and self.state[2] == s:
            if self.is_valid_turn(0):
                self.rate[0] == 30
        if self.state[3] == s and self.state[4] == s:
            if self.is_valid_turn(5):
                self.rate[5] == 30
        if self.state[3] == s and self.state[5] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 30
        if self.state[4] == s and self.state[5] == s:
            if self.is_valid_turn(3):
                self.rate[3] == 30
        if self.state[6] == s and self.state[7] == s:
            if self.is_valid_turn(8):
                self.rate[8] == 30
        if self.state[6] == s and self.state[8] == s:
            if self.is_valid_turn(7):
                self.rate[7] == 30
        if self.state[7] == s and self.state[8] == s:
            if self.is_valid_turn(6):
                self.rate[6] == 30
        #spalten
        if self.state[0] == s and self.state[3] == s:
            if self.is_valid_turn(6):
                self.rate[6] == 30
        if self.state[0] == s and self.state[6] == s:
            if self.is_valid_turn(3):
                self.rate[3] == 30
        if self.state[3] == s and self.state[6] == s:
            if self.is_valid_turn(0):
                self.rate[0] == 30
        if self.state[1] == s and self.state[4] == s:
            if self.is_valid_turn(7):
                self.rate[7] == 30
        if self.state[1] == s and self.state[7] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 30
        if self.state[4] == s and self.state[7] == s:
            if self.is_valid_turn(1):
                self.rate[1] == 30
        if self.state[2] == s and self.state[5] == s:
            if self.is_valid_turn(8):
                self.rate[8] == 30
        if self.state[2] == s and self.state[8] == s:
            if self.is_valid_turn(5):
                self.rate[5] == 30
        if self.state[5] == s and self.state[8] == s:
            if self.is_valid_turn(2):
                self.rate[2] == 30
        #diagonal
        if self.state[0] == s and self.state[4] == s:
            if self.is_valid_turn(8):
                self.rate[8] == 30
        if self.state[0] == s and self.state[8] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 30
        if self.state[4] == s and self.state[8] == s:
            if self.is_valid_turn(0):
                self.rate[0] == 30
        if self.state[2] == s and self.state[4] == s:
            if self.is_valid_turn(6):
                self.rate[6] == 30
        if self.state[2] == s and self.state[6] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 30
        if self.state[4] == s and self.state[6] == s:
            if self.is_valid_turn(2):
                self.rate[2] == 30
        #check angriff
        s = Player.players[1]
        # reihen
        if self.state[0] == s and self.state[1] == s:
            if self.is_valid_turn(2):
                self.rate[2] == 40
        if self.state[0] == s and self.state[2] == s:
            if self.is_valid_turn(1):
                self.rate[1] == 40
        if self.state[1] == s and self.state[2] == s:
            if self.is_valid_turn(0):
                self.rate[0] == 40
        if self.state[3] == s and self.state[4] == s:
            if self.is_valid_turn(5):
                self.rate[5] == 40
        if self.state[3] == s and self.state[5] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 40
        if self.state[4] == s and self.state[5] == s:
            if self.is_valid_turn(3):
                self.rate[3] == 40
        if self.state[6] == s and self.state[7] == s:
            if self.is_valid_turn(8):
                self.rate[8] == 40
        if self.state[6] == s and self.state[8] == s:
            if self.is_valid_turn(7):
                self.rate[7] == 40
        if self.state[7] == s and self.state[8] == s:
            if self.is_valid_turn(6):
                self.rate[6] == 40
        # spalten
        if self.state[0] == s and self.state[3] == s:
            if self.is_valid_turn(6):
                self.rate[6] == 40
        if self.state[0] == s and self.state[6] == s:
            if self.is_valid_turn(3):
                self.rate[3] == 40
        if self.state[3] == s and self.state[6] == s:
            if self.is_valid_turn(0):
                self.rate[0] == 40
        if self.state[1] == s and self.state[4] == s:
            if self.is_valid_turn(7):
                self.rate[7] == 40
        if self.state[1] == s and self.state[7] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 40
        if self.state[4] == s and self.state[7] == s:
            if self.is_valid_turn(1):
                self.rate[1] == 40
        if self.state[2] == s and self.state[5] == s:
            if self.is_valid_turn(8):
                self.rate[8] == 40
        if self.state[2] == s and self.state[8] == s:
            if self.is_valid_turn(5):
                self.rate[5] == 40
        if self.state[5] == s and self.state[8] == s:
            if self.is_valid_turn(2):
                self.rate[2] == 40
        # diagonal
        if self.state[0] == s and self.state[4] == s:
            if self.is_valid_turn(8):
                self.rate[8] == 40
        if self.state[0] == s and self.state[8] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 40
        if self.state[4] == s and self.state[8] == s:
            if self.is_valid_turn(0):
                self.rate[0] == 40
        if self.state[2] == s and self.state[4] == s:
            if self.is_valid_turn(6):
                self.rate[6] == 40
        if self.state[2] == s and self.state[6] == s:
            if self.is_valid_turn(4):
                self.rate[4] == 40
        if self.state[4] == s and self.state[6] == s:
            if self.is_valid_turn(2):
                self.rate[2] == 40


    def ki_random(self):
        for i in range(0,8):
            if self.rate[i] == 0:
                self.rate[i] = random.randint(15,20)

    def ki_choose_move(self):
        cache = 0
        index = 0
        for i in range(0, 8):
            if cache < self.rate[i]:
                cache = self.rate[i]
                index = i
        return index

    def ki_main(self):
        self.ki_valid_turns()
        self.ki_all_moves()
        self.ki_random()
        return self.ki_choose_move()

    #old
    def ki_move(self, ki):
        while True:
            stelle = random.randint(0,8)
            if self.is_valid_turn(stelle):
                self.make_turn(stelle, ki)
                break

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
    players = []
    def __init__(self, symbol, name, ki):
        self.symbol = symbol
        self.name = name
        self.ki = ki
        self.players.append(self)

    @classmethod
    def start_player(cls):
        rand = random.randint(0,1)
        print(str(Player.players[rand].name) + " beginnt!")
        return Player.players[rand]

    @classmethod
    def change_player(cls, aktuell):
        if aktuell == Player.players[0]:
            return Player.players[1]
        else:
            return Player.players[0]


if __name__ == '__main__':
    player1 = Player(1, "player1", False)
    comp = Player(2, "Computer", True)
    board = Board()
    active_player = Player.start_player()
    board.print_board()
    while not board.is_full():
        if active_player.ki:
            board.ki_move(active_player)
            print("Computer: ")
            board.print_board()
            if board.check_win(active_player):
                print(str(active_player.name) + " hat gewonnen!")
                exit(0)
            active_player = Player.change_player(active_player)
        else:
            try:
                pos = int(input("Position eingeben [1 - 9]: "))
            except ValueError:
                continue
            pos = pos - 1
            if pos < 0 or pos > 8:
                print("Bitte Zahl von 0 bis 9 eingeben!")
            elif not board.make_turn(pos, active_player):
                print("ungültiger Zug!")
            else:
                board.print_board()
                if board.check_win(active_player):
                    print(str(active_player.name) + " hat gewonnen!")
                    exit(0)
                active_player = Player.change_player(active_player)
    print("Unentschieden!")