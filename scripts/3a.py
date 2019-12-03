from input_manager import get_input_data
from collections import defaultdict
data = get_input_data(3).split()
data = [wire.split(",") for wire in data]

grid = defaultdict(set)

def add_coord(coord1: tuple, coord2: tuple) -> tuple:
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])
    
def multiply_coord(coord1: tuple, coord2: tuple) -> tuple:
    return (coord1[0] * coord2[0], coord1[1] * coord2[1])

def multiply_with_int(number: int, coord: tuple) -> tuple:
    return (coord[0] * number, coord[1] * number)

insts = {
    "R": (0,1),
    "L": (0,-1),
    "U": (1,0),
    "D": (-1,0)
}
wire_id = 0
for wire in data:
    wire_id += 1
    current_pos = (0,0)
    for inst in wire:
        old_pos = current_pos
        current_pos = add_coord(current_pos, multiply_with_int(int(inst[1:]), insts[inst[0]]))
        for y in range(old_pos[1], current_pos[1]-old_pos[1]):
            for x in range(old_pos[0], current_pos[0]-old_pos[0]):
                print(x,y)
                grid[x,y].add(wire_id)
