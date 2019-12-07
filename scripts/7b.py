from input_manager import get_input_data
from itertools import permutations
import intcode
import asyncio
code = get_input_data(7)
code = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"


async def get_input(start_value: int, output: list) -> int:
    yield start_value
    for i in output:
        yield i


def test_modes(modes):
    amps = [intcode.Intcode(code) for amp in range(5)]
    outputs = [[0]] + [[]]*4

    for i in range(len(amps)):
        def add_output(_output):
            outputs[i].append(_output[-1])
        amps[i].output_callback = add_output
        amps[i].input_gen = get_input(modes[i], outputs[i])

    for i in range(len(amps)):
        asyncio.run(amps[i].run())
    return amps


loops = set()
for modes in permutations(range(5)):
    loops[(*modes,)] = test_modes(modes)[-1].output[-1]
