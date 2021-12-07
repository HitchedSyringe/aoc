# Part 1 of Day 4 of Advent of Code 2021.

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
