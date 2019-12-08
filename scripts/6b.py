from input_manager import get_input_data
from collections import defaultdict
# ["a" orbits "b"] (index 0 orbits index 1)
orbits = dict(map(lambda x: x.rstrip().split(")")[::-1], get_input_data(6, True)))

def transfer_count(child):
    if child in orbits:
        return transfer_count(orbits[child]) | {orbits[child]}
    return set()

print(len(transfer_count("YOU") ^ transfer_count("SAN")))
