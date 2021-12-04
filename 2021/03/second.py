# Part 2 of Day 3 of Advent of Code 2021.

from pathlib import Path


with open(Path(__file__).parent / "inputs.txt") as f:
    data = f.read().splitlines()


def get_rating(data, reverse=False):
    line = 0

    while len(data) > 1:
        ones = list(filter(lambda e: e[line] == "1", data))
        zeroes = list(filter(lambda e: e[line] == "0", data))

        if len(zeroes) > len(ones):
            data = zeroes if not reverse else ones
        else:
            data = ones if not reverse else zeroes

        line += 1

    return data[0]


o2 = int(get_rating(data), 2)
co2 = int(get_rating(data, reverse=True), 2)

print("Oxygen generator rating: ", o2)
print("Carbon Dioxide scrubber rating: ", co2)
print("Product of both ratings: ", o2 * co2)
