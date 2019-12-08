from input_manager import get_input_data
import intcode

print(intcode.parse(get_input_data(5), [5])[-1])