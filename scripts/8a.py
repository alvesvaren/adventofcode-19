from input_manager import get_input_data
data = get_input_data(8).rstrip()
n = 25*6
data = [data[i:i+n] for i in range(0, len(data), n)]

min_layer = min(data, key=lambda x: x.count("0"))

print(min_layer.count("1") * min_layer.count("2"))
