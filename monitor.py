import json

from telegram import Bot
from telegram.ext import Application

from server import query_info


def main():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    address = config['address']
    port = config['port']
    mointor_interval = config['telegram']['mointor_interval']
    bot_token = config['telegram']['bot_token']
    chat_id = config['telegram']['chat_id']
    last_status = None

    async def post_init(application: Application):
        await bot.send_message(chat_id=chat_id, text='Valve Server Monitor - Starting...')

    async def post_stop(application: Application):
        await bot.send_message(chat_id=chat_id, text='Valve Server Monitor - Shutting down...')

    application = (Application
            .builder()
            .token(bot_token)
            .post_init(post_init)
            .post_stop(post_stop)
            .build())

    bot = application.bot

    async def monitor_server(context):
        nonlocal last_status

        try:
            curr_status = query_info(address, port)
            if last_status != curr_status:
                if curr_status is not None:
                    await bot.send_message(chat_id=chat_id, text=f'Valve Server Monitor - Server started.\nMap name: {curr_status.map_name}\nMods: {curr_status.mods_count}')
                else:
                    await bot.send_message(chat_id=chat_id, text='Valve Server Monitor - Server stopped.')

            last_status = curr_status
        except:
            await bot.send_message(chat_id=chat_id, text='Valve Server Monitor - Exception raised!')
            raise

    job_queue = application.job_queue
    job_queue.run_repeating(monitor_server, interval=900, first=5)

    application.run_polling()


if __name__ == "__main__":
    main()