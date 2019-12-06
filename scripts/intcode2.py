from input_manager import get_input_data
# args = _mem, _input, _output, *params (param(index+2), so param 1 would be 3)

verbose = False
def _1(_mem, _input, _output, a, b, c):
    _mem[c[0]] = (a[0] if a[1] == 1 else _mem[a[0]]) + \
        (b[0] if b[1] == 1 else _mem[b[0]])

    return _mem, _input, _output


def _2(_mem, _input, _output, a, b, c):
    _mem[c[0]] = (a[0] if a[1] == 1 else _mem[a[0]]) * \
        (b[0] if b[1] == 1 else _mem[b[0]])
    return _mem, _input, _output

# store input at address


def _3(_mem, _input, _output, a):
    _mem[a[0]] = _input.pop(0)
    return _mem, _input, _output

# store param1 as output


def _4(_mem, _input, _output, a):
    _output.append(_mem[a[0]])
    return _mem, _input, _output

def _99(_mem, _input, _output):
    if verbose: print(_output)
    quit()


# memory, *params -> return
instructions = {
    1: _1,
    2: _2,
    3: _3,
    4: _4,

    99: _99,
}


def params(func) -> int:
    return func.__code__.co_argcount-3


def parse(code: str, _input: list):
    program = [*map(int, code.split(","))]
    _output = []
    jump = 0
    next_params = []
    modes = []
    next_instruction = None
    pos = -1
    while pos < len(program)-1 and (program[pos] != 99 or pos < 0):
        pos += 1
        if verbose: print("current address:", pos, "("+str(program[pos])+")")
        if jump:
            pass
            jump -= 1
            value = None
            if verbose: print("adding argument ", end="")
            if modes[jump]:
                value = (program[pos]%len(program), 1)
                if verbose: print('"intermediate', str(value[0]) + '"')
            else:
                value = (program[pos]%len(program), 0)
                if verbose: print('"adress', program[pos], "("+str(program[pos]) + ')"')
            next_params.append(value)
            continue
        else:
            if next_instruction:
                if verbose: print("running", next_instruction, "with (", *next_params, ")")
                _mem, _input, _output = next_instruction(
                    program, _input, _output, *next_params)
                next_params = []
            
            next_instruction = instructions[int(str(program[pos])[-2:])]
            jump = params(next_instruction)
            modes = [*map(int, str(program[pos])[:-2])][::-1]
            if len(modes) < jump:
                modes = modes + [0]*(jump-len(modes))
                pass
    return _output


print(parse(get_input_data(5), [1]))  # return a tuple of ints instead of a map object
