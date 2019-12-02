import requests
import os
from datetime import datetime
import json

with open("config.json") as file:
    config = json.load(file)


def get_day(number: int) -> str:
    return requests.get(f"https://adventofcode.com/2019/day/{number}/input", cookies=config["getInput"]["cookies"]).text

if __name__ == "__main__":
    input_path: str = os.path.join(os.getcwd(), "inputs")
    current_day: int = datetime.now().day

    if not os.path.exists(input_path):
        os.mkdir(input_path)

    try:
        last_day_downloaded = tuple(
            map(lambda x: int(x.rstrip(".txt")), tuple(os.walk(input_path))[0][-1]))[-1]
    except IndexError:
        last_day_downloaded = 1

    if last_day_downloaded < current_day:
        for i in range(last_day_downloaded, current_day+1):
            with open(f"./inputs/{i}.txt", "w") as file:
                file.write(get_day(i))
