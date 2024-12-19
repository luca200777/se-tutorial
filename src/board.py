import random

class Board:
    def __init__(self, s:str):
        self.s = s

    def random_move(self):
        rn_nm = random.randint(0,9)
        curr_val = self.s[rn_nm]
        print(rn_nm, curr_val)
        if (curr_val == 'x'):
            self.s[rn_nm] = 'o'
        else:
            self.s[rn_nm] = 'x'

    def move(self)->str:
        self.random_move()
        return self.s

if __name__ == '__main__':
    my_board = Board(['o', 'o', 'x', 'x', 'x', 'o', 'x', 'o', 'o'])
    print(my_board.s)
    my_board.move()
    print(my_board.s)