"""
Solution to Part 1 of Day 1 of Advent of Code 2021.
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
