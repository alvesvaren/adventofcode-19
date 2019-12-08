from input_manager import get_input_data
from collections import defaultdict
# ["a" orbits "b"] (index 0 orbits index 1)
orbits = dict(map(lambda x: x.rstrip().split(")")[::-1], get_input_data(6, True)))

def distance_from_root(child):
    if child in orbits:
        return distance_from_root(orbits[child]) + 1
    return 0

total_orbits = 0
for orbit in orbits:
    total_orbits += distance_from_root(orbit)

print(total_orbits)
