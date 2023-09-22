"""
Solution to Part 1 of Day 3 of Advent of Code 2021.
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
