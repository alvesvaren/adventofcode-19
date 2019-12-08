from input_manager import get_input_data
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

steps = {}

positions = [{}, {}]

wire_id = 0
for wire in data:
    current_pos = (0, 0)
    current_steps = -1
    for part in wire:
        old_pos = current_pos
        current_pos = add_coord(current_pos, multiply_with_int(
            int(part[1:]), insts[part[0]]))
        x, y = current_pos
        for x in range(old_pos[0], current_pos[0], sum(insts[part[0]])):
            current_steps+=1
            if (x,y) in positions[wire_id]:
                continue
            positions[wire_id][x,y]=current_steps
            
        for y in range(old_pos[1], current_pos[1], sum(insts[part[0]])):
            current_steps+=1
            if (x,y) in positions[wire_id]:
                continue
            positions[wire_id][x,y]=current_steps
            
    wire_id += 1

intersections = positions[0].keys() & positions[1].keys()
intersections.remove((0,0))
shortest = min(intersections, key=lambda x: abs(positions[0][x]) + abs(positions[1][x]))
print(abs(positions[0][shortest]) + abs(positions[1][shortest]))
