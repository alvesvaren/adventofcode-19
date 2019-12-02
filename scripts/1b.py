from input_manager import get_input_data
import math

data = get_input_data(1, True)  # Get the input for day one
data = list(map(lambda x: int(x), data))


def get_fuel(x): return math.floor(int(x)/3)-2


module_fuels = []
for module in data:
    total_fuel = 0
    current_fuel_added = module
    while current_fuel_added > 6:
        current_fuel_added = get_fuel(current_fuel_added)
        total_fuel += current_fuel_added
        print(current_fuel_added)
    module_fuels.append(total_fuel)


print(sum(module_fuels))
