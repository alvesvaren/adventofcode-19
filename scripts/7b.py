from input_manager import get_input_data
from itertools import permutations
from intcode2 import IntcodeVM
import asyncio
code = get_input_data(7)
code = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"


def get_input(start_value: int, other_vm) -> int:
    yield start_value
    for step in other_vm.output:
        yield step


# async def test_modes(modes):
#     amps = [intcode.Intcode(code) for amp in range(5)]
#     outputs = [[0]] + [[]]*4

#     for i in range(len(amps)):
#         def add_output(_output):
#             outputs[i].append(_output[-1])
#         amps[i].output_callback = add_output
#         amps[i].input_gen = get_input(modes[i], outputs[i])
#     # futures = []
#     # for i in range(len(amps)):
#     #     print(i)
#     #     futures.append(await asyncio.gather(amps[i].run()))
#     runs = [await i.run() for i in amps]
#     future = await asyncio.gather(*runs, return_exceptions=True)
#     return amps

def test_modes(modes):
    # vms = [IntcodeVM(code, ) for amp in range(5)]
    vms = []
    vms.append(IntcodeVM(code, None))
    for i in range(1, len(modes)):
        vms.append(IntcodeVM(code, get_input(modes[i], vms[i-1])))
    vms[0].input = get_input(modes[0], vms[-1])

    for vm in vms:
        for out in vm.run():
            print(out)
    
    return 


loops = {}
for modes in permutations(range(5)):
    # print(dir(asyncio.run(test_modes(modes))))
    loops[(*modes,)] = tuple(test_modes(modes)[-1])[-1]
    print(loops[(*modes,)])