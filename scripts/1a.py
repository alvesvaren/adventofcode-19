from input_manager import get_input_data
import math

data = get_input_data(1, True)  # Get the input for day one

print(sum(map(lambda x: math.floor(int(x)/3)-2, data)))
