"""
Solution to Part 1 of Day 4 of Advent of Code 2021.
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

    for board in boards:
        if board.is_winner(called):
            score = board.get_winning_score(called, number)
            print("We have a winner! The board score is", score)
            exit()

    print("No winners yet...")
