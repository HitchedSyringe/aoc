# Part 1 of Day 2 of Advent of Code 2021.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    data = f.read().splitlines()

x = 0  # Horizontal position
y = 0  # Depth

for line in data:
    direction, number = line.split(" ")

    if direction == "forward":
        x += int(number)
        print(f"Moved forward by {number} units.")
    elif direction == "up":
        y -= int(number)
        print(f"Ascended {number} units.")
    else:
        y += int(number)
        print(f"Descended {number} units.")

print(f"The submarine is currently at ({x}, {y}).")
print(f"The product of the final x and y values is {x * y}.")
