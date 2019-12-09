from input_manager import get_input_data
import intcode
import asyncio
from itertools import permutations
code = get_input_data(7)


def default_input(start_value: int):
    yield start_value
    yield 0


def get_input(start_value: int, second_value: int):
    yield start_value
    yield second_value


def test_modes(modes):
    amps = [intcode.Intcode(code) for amp in range(5)]
    amps[0].input_gen = default_input(modes[0])
    amps[0].run()
    outputs = []
    for i in range(1, len(amps)):
        prev_output = list(amps[i-1].output)
        amps[i].input_gen = get_input(modes[i], prev_output[-1])
        amps[i].run()
        outputs.append(prev_output)
    return outputs


loops = {}
for modes in permutations(range(5)):
    outputs = test_modes(modes)
    print(outputs)
    loops[(*modes,)] = outputs[-1][-1]

highest = max(loops, key=lambda x: loops[x])
print(loops[highest])
