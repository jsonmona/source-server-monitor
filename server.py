import a2s


# The appid from Steam. Set to None to ignore
# https://store.steampowered.com/app/<appid>
GAME_ID = 244850


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

    if GAME_ID is not None and info.game_id != GAME_ID:
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
