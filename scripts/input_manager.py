def get_input_data(day: int) -> str:
    with open(f'../inputs/{day}.txt') as file:
        return file.read()