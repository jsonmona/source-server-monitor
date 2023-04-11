## Source Server Monitor

A simple monitoring application for game servers using Source Engine Query.

This program is NOT for testing *the* Steam webpage!

It is tested with [Space Engineers](https://store.steampowered.com/app/244850), but it should work with most games in
theory.

### Usage
`python ping.py (address) (port)`
Ping the address and port.

`python ping.py -c`
Load address and port from `config.json`, and ping it.

`python monitor.py`
Load config from `config.json`, and monitor it.
Notify using telegram if the server starts or stops.

To use this command, you need to create a telegram bot and acquire the chat ID (the chat with only you and the bot).
Chat ID can be acquired by following steps from https://stackoverflow.com/a/50736131.

### Config format
```json
{
  "address": "(address here)",
  "port": (port here),
  "telegram": {
    "mointor_interval": (monitoring interval in seconds),
    "bot_token": "(token here)",
    "chat_id": "(chat id here)"
  }
}
```

Note that `telegram` is not required unless you want monitoring.

---
Example:
```json
{
  "address": "127.0.0.1",
  "port": 27016,
  "telegram": {
    "mointor_interval": 900,
    "bot_token": "1234567890:Some-Base64-String-Here",
    "chat_id": "9876543210"
  }
}
```
