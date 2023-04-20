import a2s

from dataclasses import dataclass, field


# The appid from Steam. Set to None to ignore
# https://store.steampowered.com/app/<appid>
GAME_ID = 244850


@dataclass
class ServerInfo:
    ping: float = field(compare=False)
    map_name: str
    mods_count: int


def query_info_raw(ip, port):
    try:
        return a2s.info((str(ip), int(port)))
    except KeyboardInterrupt:
        raise
    except:
        pass


def query_info(ip, port):
    info = query_info_raw(ip, port)
    if info is None:
        return None

    if GAME_ID is not None and info.game_id != GAME_ID:
        return None

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
        mods = 0

    return ServerInfo(ping=info.ping, map_name=info.map_name, mods_count=mods)
