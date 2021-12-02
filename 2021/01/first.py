# Part 1 of Day 1 of Advent of Code 2021.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    data = f.readlines()

previous = int(data.pop(0))

print(f"{previous} (N/A: No previous measurement)")

increased = 0

for line in data:
    line = int(line)

    if line > previous:
        print(f"{line} (increased)")
        increased += 1
    elif line < previous:
        print(f"{line} (decreased)")
    else:
        print(f"{line} (no change)")

    previous = line

print(f"Overall, {increased} measurements were larger than their previous measurement.")
