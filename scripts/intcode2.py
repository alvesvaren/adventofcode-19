from input_manager import get_input_data
from collections import defaultdict
# args = _mem, _input, _output, *params (param(index+2), so param 1 would be 3)

def _1(_mem, _input, _output, a, b, c):
    _mem[c] = a + b
    return _mem, _input, _output

def _2(_mem, _input, _output, a, b, c):
    _mem[c] = a * b
    return _mem, _input, _output

# store input at address
def _3(_mem, _input, _output, a):
    _mem[a] = _input
    return _mem, _input, _output

# store param1 as output
def _4(_mem, _input, _output, a):
    _output = a
    return _mem, _input, _output

def _99(_mem, _input, _output):
    print(_output)
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

def parse(code: str, _input):
    program = [*map(int, code.split(","))]
    _output = None
    jump = 0
    next_params = []
    modes = defaultdict(int)
    next_instruction = None
    pos = -1
    while pos < len(program) and (program[pos] != 99 or pos < 0):
        pos+=1
        print("current:", program[pos])
        if jump:
            pass
            jump -= 1
            value = None
            print("adding argument ", end="")
            if modes[jump]:
                value = program[pos]
                print('"intermediate', str(value) + '"')
            else:
                value = program[program[pos]]
                print('"adress', program[pos], "("+str(value) + ')"')
            next_params.append(value)
            continue
        else:
            if next_instruction:
                print("running", next_instruction, "with (", *next_params, ")")
                _mem, _input, _output = next_instruction(program, _input, _output, *next_params)
                next_params = []
            next_instruction = instructions[int(str(program[pos])[-2:])]
            jump = params(next_instruction)
    print(_output)

def run(code: str, _input: int):
    output: list = []
    pos = 0
    while pos < len(code) and code[pos] != 99:
        (re.match(r"(\d)(\d)(\d)(\d\d)", (5*'0')+str(code[pos]))).groups()[1]


parse("3,0,4,0,99", 1)  # return a tuple of ints instead of a map object
