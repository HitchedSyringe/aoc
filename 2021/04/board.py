"""
Bingo board class.
Copyright (C) 2021-present HitchedSyringe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


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
