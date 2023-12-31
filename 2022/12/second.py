"""
Solution to Part 2 of Day 12 of Advent of Code 2022.
Copyright (C) 2022-present HitchedSyringe

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

from _shared import calculate_steps, find_start_and_end_points


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

heightmap = [list(row) for row in content.strip().splitlines()]
starts, end = find_start_and_end_points(
    heightmap, allow_starting_at_lowest_points=True
)

step_values = []
for start in starts:
    try:
        steps = calculate_steps(start, end, heightmap)
    except RuntimeError:
        pass
    else:
        step_values.append(steps)

print("Shortest distance is: ", min(step_values))
