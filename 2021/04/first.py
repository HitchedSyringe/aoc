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

    for board in boards:
        if board.is_winner(called):
            score = board.get_winning_score(called, number)
            print("We have a winner! The board score is", score)
            exit()

    print("No winners yet...")
