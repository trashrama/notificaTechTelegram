from time import sleep
from telethon import TelegramClient
from telethon.tl import types, functions

# Remember to use your own values from my.telegram.org!
api_id = 0
api_hash = ''
bot_token = ''

client = TelegramClient('neo', api_id, api_hash)
sessaoBOT = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


async def main():
    while True:
        me = await client.get_me()
        bot = await sessaoBOT.get_me()

        chat = -1001243767423
        async for message in client.iter_messages(chat, wait_time=0):
            if (message.media_unread) == True:
                if ("S20 FE 5G" in message.message):
                    print(message.message)
                    destination_user_username = 'trashrama'
                    entity = await sessaoBOT.get_entity(destination_user_username)
                    await sessaoBOT.send_message(entity=entity, message=message.message)
                    await client.send_read_acknowledge(chat, message)
            else:
                break
        sleep(300)


with client:
    client.loop.run_until_complete(main())
