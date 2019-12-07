from input_manager import get_input_data
import intcode
import asyncio
code = get_input_data(7)


async def default_input(start_value: int):
    yield start_value
    yield 0


async def get_input(start_value: int, second_value: int):
    yield start_value
    yield second_value


def test_modes(modes):
    amps = [intcode.Intcode(code) for amp in range(5)]
    amps[0].input_gen = default_input(modes[0])
    asyncio.run(amps[0].run())
    for i in range(1, len(amps)):
        amps[i].input_gen = get_input(modes[i], amps[i-1].output[-1])
        asyncio.run(amps[i].run())
    return amps


loops = {}
for x in range(5):
    for y in range(5):
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    modes = [x, y, i, j, k]
                    if sorted(modes) == [0, 1, 2, 3, 4]:
                        loops[(*modes,)] = test_modes(modes)[-1].output[-1]

highest = max(loops, key=lambda x: loops[x])
print(loops[highest])
