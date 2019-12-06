
verbose = False


def _1(_mem, _input, _output, pos, a, b, c):
    _mem[c[0]] = (a[0] if a[1] == 1 else _mem[a[0]]) + \
        (b[0] if b[1] == 1 else _mem[b[0]])

    return _mem, _input, _output, pos


def _2(_mem, _input, _output, pos, a, b, c):
    _mem[c[0]] = (a[0] if a[1] == 1 else _mem[a[0]]) * \
        (b[0] if b[1] == 1 else _mem[b[0]])
    return _mem, _input, _output, pos


def _3(_mem, _input, _output, pos, a):
    _mem[a[0]] = _input[0]
    return _mem, _input, _output, pos


def _4(_mem, _input, _output, pos, a):
    _output.append(a[0] if a[1] == 1 else _mem[a[0]])
    return _mem, _input, _output, pos


def _5(_mem, _input, _output, pos, a, b):
    if (a[0] if a[1] == 1 else _mem[a[0]]) != 0:
        pos = (b[0] if b[1] == 1 else _mem[b[0]])
    return _mem, _input, _output, pos


def _6(_mem, _input, _output, pos, a, b):
    if (a[0] if a[1] == 1 else _mem[a[0]]) == 0:
        pos = (b[0] if b[1] == 1 else _mem[b[0]])
    return _mem, _input, _output, pos


def _7(_mem, _input, _output, pos, a, b, c):
    if (a[0] if a[1] == 1 else _mem[a[0]]) < (b[0] if b[1] == 1 else _mem[b[0]]):
        _mem[c[0]] = 1
    else:
        _mem[c[0]] = 0
    return _mem, _input, _output, pos


def _8(_mem, _input, _output, pos, a, b, c):
    if (a[0] if a[1] == 1 else _mem[a[0]]) == (b[0] if b[1] == 1 else _mem[b[0]]):
        _mem[c[0]] = 1
    else:
        _mem[c[0]] = 0
    return _mem, _input, _output, pos


def _99(_mem, _input, _output, pos):
    if verbose:
        print(_output)


# memory, *params -> return
instructions = {
    1: _1,
    2: _2,
    3: _3,
    4: _4,
    5: _5,
    6: _6,
    7: _7,
    8: _8,

    99: _99,
}


def params(func) -> int:
    return func.__code__.co_argcount-4


def parse(code: str, _input: list = []):
    program = [*map(int, code.split(","))]
    _output = []
    jump = 0
    next_params = []
    modes = []
    history = {}
    next_instruction = None
    pos = -1
    while pos < len(program)-1 and (program[pos] != 99 or pos < 0):
        pos += 1
        if verbose:
            print("current address:", pos, "("+str(program[pos])+")")
        if jump:
            pass
            jump -= 1
            value = None
            if verbose:
                print("adding argument ", end="")
            if modes[::-1][jump]:
                value = (program[pos % len(program)], 1)
                if verbose:
                    print('"intermediate', str(value[0]) + '"')
            else:
                value = (program[pos] % len(program), 0)
                if verbose:
                    print('"adress', program[pos],
                          "("+str(program[pos]) + ')"')
            next_params.append(value)
            continue
        else:
            if next_instruction:
                if verbose:
                    print("running", next_instruction,
                          "with (", *next_params, ")")
                history.update({pos: {
                    "instruction": next_instruction,
                    "params": next_params,
                }})
                old_pos = pos
                _mem, _input, _output, pos = next_instruction(
                    program, _input, _output, pos, *next_params)
                next_params = []
                if old_pos != pos:
                    if verbose:
                        print("new pos!", pos, "(from", str(old_pos)+")")

            next_instruction = instructions[int(str(program[pos])[-2:])]
            jump = params(next_instruction)
            modes = [*map(int, str(program[pos])[:-2])][::-1]
            if len(modes) < jump:
                modes = modes + [0]*(jump-len(modes))
                pass
    if verbose:
        print(_mem)
    return _output


if __name__ == "__main__":
    verbose = True
    print(parse(input("Code: "), [int(input("Input: "))]))
