from input_manager import get_input_data


def reset_memory_with_start_args(a,b):
    data = get_input_data(2)
    data = list(map(int, data.split(",")))
    data[1] = a
    data[2] = b
    return data

instructions = {1: lambda a, b: a+b, 2: lambda a, b: a*b}

def program(data):
    for i in range(0, len(data), 4):
        if data[i] == 99:
            # print(data[0])
            break
        instruction = instructions[data[i]]
        value = instruction(data[data[i+1]], data[data[i+2]])
        data[data[i+3]] = value
    return data

start_data = reset_memory_with_start_args(1,1)
for i in range(len(start_data)):
    for j in range(len(start_data)):
        data = reset_memory_with_start_args(i,j)
        if program(data)[0] == 19690720:
            print(100*i+j)
            quit()
