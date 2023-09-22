"""
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


import argparse
from pathlib import Path

import requests


_TEMPLATE: str = '''\
"""
Solution to Part {0} of Day {1} of Advent of Code {2}.
Copyright (C) {3}-present HitchedSyringe

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


path = Path(__file__).parent / "inputs.txt"
content = path.read_text()

'''


def get_session() -> str:
    with open(".session") as f:
        return f.read().strip()


def fetch_input(year: int, day_number: int) -> bytes:
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day_number}/input",
        cookies={"session": get_session()}
    )
    response.raise_for_status()

    return response.content


def create_day(year: int, day_number: int) -> None:
    path = Path(__file__).parent / str(year) / format(day_number, ">02")
    path.mkdir(exist_ok=True)

    puzzle_input = fetch_input(year, day_number)
    path.joinpath("inputs.txt").write_bytes(puzzle_input)

    for part, name in enumerate(("first.py", "second.py"), 1):
        path.joinpath(name).write_text(_TEMPLATE.format(part, day_number, year))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", "-y", type=int, required=True)
    parser.add_argument("--day-number", "-dn", type=int, required=True)

    args = parser.parse_args()

    create_day(args.year, args.day_number)
