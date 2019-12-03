from input_manager import get_input_data
from collections import defaultdict
import math
data = get_input_data(3).split()
data = [wire.split(",") for wire in data]


def add_coord(coord1: tuple, coord2: tuple) -> tuple:
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


def multiply_with_int(number: int, coord: tuple) -> tuple:
    return (coord[0] * number, coord[1] * number)


insts = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0)
}

positions = [set(), set()]

wire_id = 0
for wire in data:
    current_pos = (0, 0)
    for part in wire:
        old_pos = current_pos
        current_pos = add_coord(current_pos, multiply_with_int(
            int(part[1:]), insts[part[0]]))
        x, y = current_pos
        for x in range(old_pos[0], current_pos[0], sum(insts[part[0]])):
            positions[wire_id].add((x, y))
        for y in range(old_pos[1], current_pos[1], sum(insts[part[0]])):
            positions[wire_id].add((x, y))
    wire_id += 1

intersections = positions[0] & positions[1]
intersections.remove((0, 0))

print(sum(min(intersections, key=lambda x: sum((abs(x[0]), abs(x[1]))))))
