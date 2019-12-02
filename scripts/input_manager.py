def get_input_data(day: int, in_list_form: bool=False) -> str:
    with open(f'../inputs/{day}.txt') as file:
        return file.read() if not in_list_form else file.readlines()