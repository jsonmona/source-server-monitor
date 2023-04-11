import sys
import json

from server import check_alive


USAGE = f'Usage: {sys.argv[0]} [-c] [address] [port]'


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-c':
        with open('config.json', 'r', encoding='utf-8') as f:
            obj = json.load(f)

        check_alive(obj['address'], obj['port'])
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = sys.argv[2]

        try:
            port = int(port)
        except ValueError:
            print(USAGE)
            return

        check_alive(address, port)
    else:
        print(USAGE)


if __name__ == '__main__':
    main()
