# Part 2 of Day 2 of Advent of Code 2021.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    data = f.read().splitlines()

x = 0  # Horizontal position
y = 0  # Depth
aim = 0

for line in data:
    direction, number = line.split(" ")

    number = int(number)

    if direction == "forward":
        x += number
        y += number * aim
        print(f"Moved forward by {number} units.")
        print(f"Descended by {number * aim} units.")
    elif direction == "up":
        aim -= number
        print(f"Aim decreased by {number} units.")
    else:
        aim += number
        print(f"Aim increased by {number} units.")

print(f"The submarine is currently at ({x}, {y}), with an aim of {aim}.")
print(f"The product of the final x and y values is {x * y}.")
