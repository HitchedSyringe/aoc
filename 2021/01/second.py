# Part 2 of Day 1 of Advent of Code 2021.

import collections
from itertools import islice
from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    data = [int(x) for x in f.readlines()]

previous = sum(data[:3])

print(f"{previous} (N/A: No previous measurement)")

# itertools recipe from https://docs.python.org/3/library/itertools.html#itertools.islice
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)

    if len(window) == n:
        yield tuple(window)

    for x in it:
        window.append(x)
        yield tuple(window)

increased = 0

for triple in sliding_window(data[1:], 3):
    triple_sum = sum(triple)

    if triple_sum > previous:
        print(f"{triple_sum} (increased)")
        increased += 1
    elif triple_sum < previous:
        print(f"{triple_sum} (decreased)")
    else:
        print(f"{triple_sum} (no change)")

    previous = triple_sum

print(f"Overall, {increased} sums were larger than their previous sum.")
