"""
Shared components for Day 12 solutions.
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


from typing import Generator, List, Tuple, Union, overload


class PointState:
    """Represents a 2D point with a step value from the starting position.

    Attributes
    -----------
    position: Tuple[:class:`int`, :class:`int`]
        The x and y coordinates of the point on the heightmap.
    steps_from_start: :class:`int`
        The number of steps from the starting point on the heightmap.
    """

    __slots__: Tuple[str, str] = (
        "position",
        "steps_from_start",
    )

    def __init__(self, x: int, y: int) -> None:
        self.position: Tuple[int, int] = (x, y)
        self.steps_from_start: int = 0

    def find_valid_moves(
        self, heightmap: List[List[str]]
    ) -> Generator["PointState", None, None]:
        """Yields adjacent points which can be moved to.

        Parameters
        -----------
        heightmap: List[List[:class:`str`]]
            A list of list of strings denoting the heightmap for the area.

        Yields
        -------
        :class:`PointState`
            A valid point which can be moved to.
        """
        x, y = self.position
        for new_x, new_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                (0 <= new_x < len(heightmap[0]) and 0 <= new_y < len(heightmap))
                and ord(heightmap[new_y][new_x]) - ord(heightmap[y][x]) <= 1
            ):
                point = PointState(new_x, new_y)
                point.steps_from_start = self.steps_from_start + 1
                yield point


def calculate_steps(
    start: PointState, end: PointState, heightmap: List[List[str]]
) -> int:
    """Calculates the shortest number of steps to move from a given
    start point to a given end point.

    Parameters
    -----------
    start: :class:`PointState`
        The starting position.
    end: :class:`PointState`
        The ending position.
    heightmap: List[List[:class:`str`]]
        A list of list of strings denoting the heightmap for the area.

    Returns
    --------
    :class:`int`
        The number of steps required to move from the start point to
        the end point.

    Raises
    -------
    RuntimeError
        The number of steps could not be calculated.
    """
    queue = [start]
    known = {start.position}

    while queue:
        current = queue.pop(0)
        for move in current.find_valid_moves(heightmap):
            position = move.position

            if position not in known:
                known.add(position)
                queue.append(move)

            if position == end.position:
                return move.steps_from_start

    raise RuntimeError("Cannot find path to end point.")


@overload
def find_start_and_end_points(
    heightmap: List[List[str]],
) -> Tuple[PointState, PointState]:
    ...


@overload
def find_start_and_end_points(
    heightmap: List[List[str]],
    allow_starting_at_lowest_points: bool = True,
) -> Tuple[List[PointState], PointState]:
    ...


def find_start_and_end_points(
    heightmap: List[List[str]],
    allow_starting_at_lowest_points: bool = False,
) -> Tuple[Union[PointState, List[PointState]], PointState]:
    """Finds the start and end points of the given heightmap.

    Parameters
    -----------
    heightmap: List[List[:class:`str`]]
        A list of list of strings denoting the heightmap for the area.
    allow_starting_at_lowest_points: :class:`bool`
        Whether or not to consider the lowest points, denoted as `a`,
        as start points. Defaults to ``False``.

    Returns
    --------
    Tuple[Union[:class:`PointState`, List[:class:`PointState`]], :class:`PointState`]
        The start and end points.

    Raises
    -------
    RuntimeError
        The start and end points could not be determined.
    """
    starts = []
    end = None

    for row, line in enumerate(heightmap):
        for column, letter in enumerate(line):
            if letter == "E":
                end = PointState(column, row)
                heightmap[row][column] = "z"
            elif letter == "S":
                heightmap[row][column] = "a"
                starts.append(PointState(column, row))
            elif allow_starting_at_lowest_points and letter == "a":
                starts.append(PointState(column, row))

    if starts and end is not None:
        if len(starts) == 1:
            starts = starts[0]
        return starts, end

    raise RuntimeError("Could not find start or end points.")
