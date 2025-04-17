import json
from os import system
system("clear")


def print_code(data, indent=4):
    print(json.dumps(data, indent=indent))
