"""
Solution to Part 2 of Day 4 of Advent of Code 2021.
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


from pathlib import Path

from board import Board


with open(Path(__file__).parent / "inputs.txt") as f:
    numbers, boards = f.read().split("\n", 1)


called = set()

numbers = [int(n) for n in numbers.split(",")]
boards = [Board(b) for b in boards.split("\n" * 2)]


for number in numbers:
    called.add(number)
    print(number, "was called!")

    if len(boards) != 1:
        boards = [b for b in boards if not b.is_winner(called)]
        continue

    last_board = boards[0]

    if last_board.is_winner(called):
        score = last_board.get_winning_score(called, number)
        print("The last winning board's score is", score)
        exit()
