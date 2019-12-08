from input_manager import get_input_data
from collections import defaultdict
data = get_input_data(8).rstrip()
# data = "0222112222120000"
x_w, y_w = 25, 6
n = x_w * y_w
data = [data[i:i+n] for i in range(0, len(data), n)]


layers = defaultdict(str)
for i in range(len(data)):
    for y in range(y_w):
        for x in range(x_w):
            layers[i] += data[i][(y*x_w)+x]
        layers[i]+="\n"

layers = [layer.splitlines() for layer in layers.values()]
final_layer = ["2"*x_w for i in range(y_w)]
# print(final_layer)
for layer in layers[::-1]:
    for y in range(y_w):
        for x in range(x_w):
            curr_pixel = layer[y][x]
            final_pixel = final_layer[y][x]
            if curr_pixel != "2":   
                final_layer[y] = list(final_layer[y])
                final_layer[y][x] = curr_pixel
                final_layer[y] = "".join(final_layer[y])

print("\n"+"\n".join(final_layer).replace("2", "?").replace("0", " ").replace("1", "X"))
