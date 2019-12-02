from input_manager import get_input_data


data = get_input_data(2)
data = list(map(int, data.split(",")))
data[1] = 12
data[2] = 2

instructions = {1: lambda a, b: a+b, 2: lambda a, b: a*b}

for i in range(0, len(data), 4):
    if data[i] == 99:
        break
    instruction = instructions[data[i]]
    value = instruction(data[data[i+1]], data[data[i+2]])
    data[data[i+3]] = value

print(data[0])
