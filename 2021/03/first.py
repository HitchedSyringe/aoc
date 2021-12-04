# Part 1 of Day 3 of Advent of Code 2021.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    data = f.read().replace("\n", "")

gamma = ""
epsilon = ""

for x in range(12):
    column = data[x::12]

    epsilon += (common := max(column, key=lambda x: column.count(x)))

    print(f"Most common bit (epsilon) for column {x + 1} was {common}.")

    gamma += "1" if common == "0" else "0"

epsilon = int(epsilon, 2)
gamma = int(gamma, 2)

print(f"Epsilon value: {epsilon}")
print(f"Gamma value: {gamma}")
print(f"Power Consumption: {epsilon * gamma}")
