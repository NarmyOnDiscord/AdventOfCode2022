# Rucksack Reorganization
# https://adventofcode.com/2022/day/3

import string
from typing import Iterable

def calculate_item_priority(item: str):
    if len(item) != 1:
        raise ValueError("item must be a one-character-long string")
    if item not in string.ascii_letters:
        raise ValueError("item must be a letter")

    return string.ascii_letters.index(item) + 1

def chunks(iter: Iterable, size: int):
    """Yield successive sized chunks from iter."""
    for i in range(0, len(iter), size):
        yield iter[i : i + size]

    
# Part 1

total_points = 0

input_ = open("Day 3/input.txt", "r")
for line, content in enumerate(input_, 1):
    content = content.removesuffix("\n")

    firstpart, secondpart = (
        content[: int(len(content) / 2)],
        content[int(len(content) / 2) :],
    )
    common_item = list(set(firstpart).intersection(set(secondpart)))[0]
    common_item_priority = calculate_item_priority(common_item)
    total_points += common_item_priority

print(total_points)
input_.close()

# Part 2

input_ = open("Day 3/input.txt", "r")
lines = input_.read().splitlines()

total_points = 0

for group in chunks(lines, 3):
    print(group)
    firstpart, secondpart, thirdpart = group
    common_items = set(firstpart).intersection(set(secondpart), set(thirdpart))
    print
    common_item = list(common_items)[0]
    common_item_priority = calculate_item_priority(common_item)
    total_points += common_item_priority

print(total_points)