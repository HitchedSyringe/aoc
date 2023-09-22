"""
Solution to Part 1 of Day 2 of Advent of Code 2021.
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
