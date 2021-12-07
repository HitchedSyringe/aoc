
# The bingo board class.

class Board:

    # I didn't use numpy and now I must suffer.
    def __init__(self, board_str):
        cells = [int(c) for r in board_str.split("\n") for c in r.split(" ") if c]

        self.cells = set(cells)

        rows = [cells[5 * x:5 + 5 * x] for x in range(5)]

        self.lines = rows + list(zip(*rows))

    def is_winner(self, called):
        return any(set(l) <= called for l in self.lines)

    def get_winning_score(self, called, last_number):
        return sum(self.cells - called) * last_number
