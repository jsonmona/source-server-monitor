import sys
import json

from server import query_info


USAGE = f'Usage: {sys.argv[0]} [-c] [address] [port]'


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-c':
        with open('config.json', 'r', encoding='utf-8') as f:
            obj = json.load(f)

        print(query_info(obj['address'], obj['port']))
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = sys.argv[2]

        try:
            port = int(port)
        except ValueError:
            print(USAGE)
            return

        print(query_info(address, port))
    else:
        print(USAGE)


if __name__ == '__main__':
    main()
