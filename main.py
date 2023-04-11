import a2s
import sys
import json


GAME_NAME = 'Space Engineers'
USAGE = f'Usage: {sys.argv[0]} [-c] [address] [port]'


def query_info(ip, port):
    try:
        return a2s.info((str(ip), int(port)))
    except KeyboardInterrupt:
        raise
    except:
        pass


def check_alive(ip, port):
    info = query_info(ip, port)
    if info is None:
        return False

    mods = None
    for now in info.keywords.split(' '):
        if not now.startswith('mods'):
            continue

        try:
            now_mods = int(now[4:])
        except ValueError:
            continue

        if mods is not None:
            # Duplicate mods entry found
            mods = None
            break

        mods = now_mods

    if mods is None:
        mods = '(Unknown)'

    print(f'Map: "{info.map_name}"  Ping: {info.ping:.1f}  Mods: {mods}')

    return True


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
