import json
from pprint import pprint


def load_data(filepath):
    with open(filepath) as f:
        data = f.read()
    f.closed
    return json.loads(data)


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    data = load_data('../json.json')
    pretty_print_json(data)